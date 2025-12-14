from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import csv
import os

class CSVAnalyzerInput(BaseModel):
    file_path: str = Field(..., description="Path to CSV file with opponents data")
    weight_category: str = Field(..., description="Boxer's weight category to filter")
    boxer_record: str = Field(..., description="Boxer's win/loss ratio (format: X-Y)")

class CSVAnalyzerTool(BaseTool):
    name: str = "CSV Opponent Analyzer"
    description: str = "Analyzes CSV data to find suitable boxing opponents"
    args_schema: Type[BaseModel] = CSVAnalyzerInput

    def _run(self, file_path: str, weight_category: str, boxer_record: str) -> list:
            # Aggiungi questo controllo aggiuntivo
            if not file_path.startswith('/'):
                file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_path))
            file_path = "src/boxe1_project/data/opponents.csv"
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                opponents = [row for row in reader 
                            if row['categoria_peso'] == weight_category
                            and self._compare_records(row['record'], boxer_record)]
                
                sorted_opponents = sorted(opponents, 
                                        key=lambda x: int(x['ranking']))
                return sorted_opponents[:3]
        
                    

    def _compare_records(self, opponent_record: str, boxer_record: str) -> bool:
        o_wins, o_losses = map(int, opponent_record.split('-'))
        b_wins, b_losses = map(int, boxer_record.split('-'))
        return (o_wins <= b_wins) and (o_losses >= b_losses)