# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BoxingCrew():
    """Crew per la selezione dell'avversario e la strategia di allenamento per il pugile"""

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            verbose=True,
            # Per ora non utilizziamo tool esterni
        )

    @agent
    def coach(self) -> Agent:
        return Agent(
            config=self.agents_config['coach'],
            verbose=True
        )

    @task
    def selection_task(self) -> Task:
        return Task(
            config=self.tasks_config['selection_task'],
        )

    @task
    def training_task(self) -> Task:
        return Task(
            config=self.tasks_config['training_task'],
            output_file='training_strategy.md'
        )

    @crew
    def crew(self) -> Crew:
        """Crea la crew che esegue i task in sequenza: selezione dell'avversario e definizione della strategia di allenamento"""
        return Crew(
            agents=self.agents,  # I due agent vengono creati tramite i decoratori @agent
            tasks=self.tasks,    # I task vengono creati tramite i decoratori @task
            process=Process.sequential,
            verbose=True,
        )
