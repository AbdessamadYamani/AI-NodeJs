from langchain.tools import tool


@tool("Create File with Code")
def create_file_with_code(filename, code):
    """
    Creates a file with the given filename and writes the provided code to it.
    
    Parameters:
    filename (str): The name of the path of the file with the filename to create (including extension)
    code (str): The code content to write to the file
    
    """
    try:
        with open(filename, 'w') as file:
            file.write(code)
        return f"File '{filename}' created successfully!"
    except Exception as e:
        return f"Error: Failed to create file '{filename}'. Reason: {str(e)}"
