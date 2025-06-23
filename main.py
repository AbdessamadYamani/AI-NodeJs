from crewai import Crew
from agents import AllAgents
from tasks import AllTasks
import configs as config
from crewai.process import Process


# Instantiate AllAgents and AllTasks with the OpenAI API key
all_agents = AllAgents(openai_api_key=config.openai_api_key)
all_tasks = AllTasks(openai_api_key=config.openai_api_key)


project_manager = all_agents.ProjectManagerAgent()
core_developer = all_agents.CoreDeveloperAgent()
api_developer = all_agents.APIDevAgent()
# testing_specialist = all_agents.TestingAgent()
# config_specialist = all_agents.ConfigurationAgent()
# Create tasks with dependencies
setup_task = all_tasks.setup_project_structure(project_manager)
core_task = all_tasks.implement_core_server(core_developer, [setup_task])
api_task = all_tasks.setup_api_routes(project_manager,[setup_task])
# test_task = all_tasks.implement_tests(testing_specialist, [api_task])
# config_task = all_tasks.setup_configuration(config_specialist, [setup_task])
# Create crew with all agents and tasks
crew = Crew(
    agents=[
        project_manager,
    ],
    tasks=[
        setup_task,
        api_task,
    ],
    cache=True,
    verbose=True
)


result = crew.kickoff()
print(result)