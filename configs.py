import os
from getpass import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# Dictionary to store the keys once fetched
_api_keys = {}

def _prompt_for_key_if_needed(key_name: str, service_name: str) -> str:
    """Prompts for a key if it's not in the cache and returns it."""
    if key_name not in _api_keys:
        prompt_message = f"Please enter your {service_name} API key for '{key_name}': "
        key = getpass(prompt_message)
        if not key:
            raise ValueError(f"API key for {key_name} cannot be empty.")
        _api_keys[key_name] = key
    return _api_keys[key_name]

def get_groq_api_key(model_identifier: str) -> str:
    """Gets a Groq API key for a specific model identifier."""
    return _prompt_for_key_if_needed(f"groq_key_for_{model_identifier}", "Groq")

def get_serper_api_key() -> str:
    """Gets the Serper API key and sets the environment variable."""
    key = _prompt_for_key_if_needed("serper_api_key", "Serper")
    os.environ["SERPER_API_KEY"] = key
    return key

def get_gemini_api_key() -> str:
    """Gets the Google Gemini API key."""
    return _prompt_for_key_if_needed("gemini_api_key", "Google Gemini")

# The key in LLM_tool.py and test.py was the same as for llmLlaMa5.
# We'll use a shared identifier to ensure we only ask for it once.
LLM_TOOL_AND_AGENT_KEY_ID = "llm_tool_and_agent_5"

def get_llm_tool_groq_key() -> str:
    """Gets the Groq API key for the LLM tool."""
    return get_groq_api_key(LLM_TOOL_AND_AGENT_KEY_ID)

# llama-3.1-8b-instant	, llama3-8b-8192,llama-3.1-70b-versatile
llmLlaMa0 = ChatGroq(api_key=get_groq_api_key("agent_0_llama3-70b"), model="llama3-70b-8192")
llmLlaMa1 = ChatGroq(api_key=get_groq_api_key("agent_1_llama-3.2-90b"), model="llama-3.2-90b-text-preview")
llmLlaMa2 = ChatGroq(api_key=get_groq_api_key("agent_2_llama3-groq-tool-use"), model="llama3-groq-70b-8192-tool-use-preview")
llmLlaMa3 = ChatGroq(api_key=get_groq_api_key("agent_3_gemma2-9b"), model="gemma2-9b-it")
llmLlaMa4 = ChatGroq(api_key=get_groq_api_key("agent_4_mixtral-8x7b"), model="mixtral-8x7b-32768")
llmLlaMa5 = ChatGroq(api_key=get_groq_api_key(LLM_TOOL_AND_AGENT_KEY_ID), model="llama-3.2-90b-text-preview")
# gemini
llmGemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=get_gemini_api_key())

# For backward compatibility with main.py, which uses openai_api_key
# We'll point it to the Gemini key.
openai_api_key = get_gemini_api_key()