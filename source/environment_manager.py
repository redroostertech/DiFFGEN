from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Accessing variables
env = os.getenv('ENV')

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_engine = os.getenv('OPENAI_ENGINE')
prompt_path = os.getenv('PROMPT_PATH')

# Use the variables in your script
if env == "LOCAL":
    print(f"""
Keys
=====
Environment: {env}
Open AI API Key: {openai_api_key}
Open AI Engine: {openai_engine}
Prompt for Path: {prompt_path}
          """)
    