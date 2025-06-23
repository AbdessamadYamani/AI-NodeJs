from crewai import Task
import tools.cmd_tool as cmd_tool
import tools.create_files as create_files
import tools.LLM_tool as LLM_tool

Project ="""
The project is creating 3  end points one shows Hi , the other take from the url the 2 numbers and shows the sum , the 3th one take the 2 numbers from the url and shows the multiplication of them.

"""
ROLES="""
+ Ignore this yask if it s not nessesary to run the project
+ create each file with its code 
+ Before creating any file give to the tool the whole path not the relative path.
+ the tool thta gives you the code use it to cpy the code and put it in the files following this structure :
send the project description and the structure.the tool will give you the code of each file and you copie the code and put it in the files.
"""
class AllTasks():
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def create_code(self, agent, context):
        description = f"""
        You should create the code for each file in the project architecture and make sure to write the code in a good way so it does not cause an error.
        You can use only CMD and you are in the project directory. You can explore the project architecture and folders as you want using CMD commands. The main point is to create the code for each file in the project architecture.
        NOTE: For each file, create the whole code and push it to the file, do not write the code line by line into the file.
        The objective is to create a project that shows "Hi" in the default API.

        Use this CMD to put the code in the file [echo [the code] > File name.js].
        When you are done with all files, run the server.
        """
        return Task(
            description=description,
            expected_output="Report of the creation of the project architecture",
            output_file="report_for_code.md",
            tools=[cmd_tool.execute_command_silently],
            agent=agent,
            context=context
        )

    def create_project_arch(self, agent):
        description = f"""
        1- Your ultimate goal is to create a basic Node.js project to show "Hello world" in the browser by following these instructions.
        + Create the architecture of the Node.js project with all necessary files and folders needed to run the server. Do not forget to use npm init -y to create the package.json file.
        Note that CMD is in Windows OS.
        + You are already in the project directory, so do not recreate it.
        + If you need to install a library, you can do it.
        + When you create the architecture, create all the important folders based on the best practices for Node.js.
        + Make sure to create index.js as the start page of the server.
        + Each time you create a file, add its code using this CMD: [echo [the code] > File name.js].
        + When you finish, run npm start to start the server.
        """
        return Task(
            description=description,
            expected_output="Report of the creation of the project architecture",
            output_file="report.md",
            tools=[cmd_tool.execute_command_silently],
            agent=agent
        )
#######################################################################################################
    def setup_project_structure(self, agent):
        return Task(
            description=f"""
            Initialize the Node.js project and create the basic folder structure based on the nature of the project :
            0: You are already in the project directory.
            1. start from initialize the project
            2. Create all necessary directories based on the project.
            3. Set up .gitignore and basic README.md where you describe the project
            4. install the project with essential dependencies if needed
            
            Use only CMD commands and ensure you're in the project directory.
Project idea : {Project} """,
            expected_output="Complete project structure setup report",
            output_file="setup_report.md",
                        tools=[cmd_tool.execute_command_silently],

            agent=agent,
        )

    def implement_core_server(self, agent, context):
        return Task(
            description="""
            Create the core server files if needed else you can ignore it:
            0: See the project folders to localise the folder you have to create the files into
            1. Create index.js with server initialization with the code using the tool that create the file with the code
            2. Set up app.js with Express configuration with using the tool that create the file with the code
            3. Implement basic middleware setup if needed
            4. Create the 'Hello World' endpoint using only using the tool that create the file with the code

Use : the tool that create the file with the code , give it as parameter the path of the file after getting it using cmd
Project idea : [The project is creating 3  end points one shows Hi , the other take from the url the 2 numbers and shows the sum , the 3th one take the 2 numbers from the url and shows the multiplication of them.]
Roles : + Ignore this yask if it s not nessesary to run the project
+ Do not thik so much because it comsume Tokenz
+ Delagate task to other Agent if need
+ Before creating any file give to the tool the whole path not the relative path.
+ the tool thta gives you the code use it to cpy the code and put it in the files following this structure :
send the project description and the structure.the tool will give you the code of each file and you copie the code and put it in the files.

            """,
            expected_output="Core server implementation report",
            output_file="core_implementation_report.md",
            agent=agent,
                        tools=[cmd_tool.execute_command_silently,create_files.create_file_with_code],
            context=context
        )

    def setup_api_routes(self, agent, context):
        return Task(
            description=f"""
            For all the folder of the project create the code for each one and put it in the file based on the logic of the project:
Use : the tool that create the file with the code , give it as parameter the path of the file after getting it using cmd.
+ the tool that Get the code of the project files give it the srtucture of the project and the description of the project and it will give you the code of each file where you get the code and create the file using cmd tool and put the code in the file using the Create File with Code tool.
Project idea : {Project}
Roles : {ROLES}
            """,
            expected_output="API routes setup report",
            output_file="api_setup_report.md",
            agent=agent,
                        tools=[cmd_tool.execute_command_silently,create_files.create_file_with_code],

            context=context
        )

    def implement_tests(self, agent, context):
        return Task(
            description="""
            Create test suites if needed else you can ignore it using only cmd tool:
            1. Set up test directory structure
            2. Create unit tests for core functionality
            3. Implement integration tests
            4. Set up test configuration

Use : the tool that create the file with the code , give it as parameter the path of the file after getting it using cmd
Project idea : {Project}
Roles : {ROLES}
            """,
            expected_output="Testing implementation report",
            output_file="test_implementation_report.md",
            agent=agent,
                        tools=[cmd_tool.execute_command_silently,create_files.create_file_with_code],

            context=context
        )

    def setup_configuration(self, agent, context):
        return Task(
            description="""
            Set up project configuration if needed else you can ignore it using only cmd tool:
            1. Create configuration files
            2. Set up environment variables
            3. Implement config loading logic
            4. Create development and production configs
			5. Create the Docker file for the project.
Use : the tool that create the file with the code , give it as parameter the path of the file after getting it using cmd
Project idea : {Project}
Roles : {ROLES}
            """,
            expected_output="Configuration setup report",
            output_file="config_setup_report.md",
            agent=agent,
                        tools=[cmd_tool.execute_command_silently,create_files.create_file_with_code],

            context=context
        )
