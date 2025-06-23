from groq import Groq
from langchain.tools import tool
import configs

@tool("Get the code of the project files")
def get_groq_response(prompt):
    """
    This tool used to get the code of the project files based on the project description and the architecture of the project , i have one parameter named prompt
    """
    api_key = configs.get_llm_tool_groq_key()
    Additional="i will give you the architecture of the NODE.js Project + the Description of the project and you should give me the code of each file and for which folder"+prompt

    client = Groq(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": Additional,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content
