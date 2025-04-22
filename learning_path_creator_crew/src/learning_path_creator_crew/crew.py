from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from learning_path_creator_crew.tools.DuckDuckGoSearchTool import DuckDuckGoSearchTool

from learning_path_creator_crew.utils.utils import read_crew_settings

@CrewBase
class LearningPathCreator():
    """LearningPathCreator crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    crew_config = 'config/settings.yaml'

    # Load the crew configuration file
    crew_config = read_crew_settings(crew_config)

    duckduckgo_search_tool = DuckDuckGoSearchTool(crew_config['verbose'])

    @agent
    def goal_clarification_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['goal_clarification_agent'],
            tools=[self.duckduckgo_search_tool],
            verbose=self.crew_config['verbose'],
            tempreature=self.crew_config['tempreature'],
        )

    @agent
    def quality_relevance_assessor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_relevance_assessor_agent'],
            tools=[self.duckduckgo_search_tool],
            verbose=self.crew_config['verbose'],
            tempreature=self.crew_config['tempreature'],
        )

    @agent
    def curriculum_design_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_design_agent'],
            verbose=self.crew_config['verbose'],
            tempreature=self.crew_config['tempreature'],
        )

    @agent
    def learning_path_presenter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_path_presenter_agent'],
            verbose=self.crew_config['verbose'],
            tempreature=self.crew_config['tempreature'],
        )

    # ################################################################################ #

    @task
    def define_learning_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['define_learning_requirements'],
        )

    @task
    def discover_potential_resources(self) -> Task:
        return Task(
            config=self.tasks_config['discover_potential_resources'],
        )

    @task
    def evaluate_and_filter_resources_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_and_filter_resources'],
        )
    
    @task
    def design_the_learning_path_structure_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_the_learning_path_structure'],
        )
    
    @task
    def compile_the_final_learning_plan_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_the_final_learning_plan_report'],
            output_file='learning_plan_report.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LearningPathCreator crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=self.crew_config['verbose'],
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
