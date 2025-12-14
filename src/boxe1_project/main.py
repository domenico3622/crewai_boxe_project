#!/usr/bin/env python
import sys
import os
import warnings
from datetime import datetime
from boxe1_project.crew import BoxingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def read_csv_as_string(csv_path: str) -> str:
    with open(csv_path, 'r', encoding='utf-8') as f:
        return f.read()

def run():
    """
    Avvia la crew per selezionare l'avversario e definire la strategia di allenamento.
    """
    csv_path = 'src/boxe1_project/data/opponents.csv'
    csv_content = read_csv_as_string(csv_path)
    
    inputs = {
        'csv_file': csv_path,  # Se necessario per altre funzioni
        'stringa_csv': csv_content,  # Placeholder per l'intero contenuto del CSV
        'boxer': {
            'nome': "Franchino Er Criminale",
            'categoria_peso': 'Heavyweight',
            'vittorie': 38,
            'sconfitte': 2,
        }
    }
    BoxingCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
