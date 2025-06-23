import subprocess
import os
from langchain.tools import tool

@tool("Execute CMD")
def execute_command_silently(command: str):
    """
    This tool used to execute any cmd from the parameters and returns output or error message
    it have as a parameter the command 
    """
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to the "Project" folder
    project_directory = os.path.join(script_directory, "Project")
    
    # Ensure the Project directory exists
    os.makedirs(project_directory, exist_ok=True)

    try:
        # Start the subprocess with a specified working directory
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            shell=True, 
            text=True,
            cwd=project_directory  # Execute in Project directory
        )

        # Capture output and errors
        stdout, stderr = process.communicate()

        # If there's an error, return it
        if stderr:
            return f"Error: {stderr.strip()}"
            
        # If successful, return the output
        if stdout:
            return stdout.strip()
            
        # If no output but successful execution
        return "Command executed successfully"

    except Exception as e:
        return f"Exception occurred: {str(e)}"
