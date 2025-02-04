# Stores project settings such as:
# Database connection URL
# Firebase API keys
# Environment variables

from dotenv import load_dotenv
import os
from langchain_huggingface.llms import HuggingFaceEndpoint

load_dotenv()

hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_api_key:
  raise ValueError("Hugging Face Api Key not found in .env file")

hf_repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

hf_temperature = 0.7
hf_max_new_tokens = 500

def get_llm():
  return HuggingFaceEndpoint(
    repo_id=hf_repo_id,
    temperature=hf_temperature,
    max_new_tokens=hf_max_new_tokens,
    model_kwargs={"token":hf_api_key}
  )

sql_prompt = """
Convert the following user query into an equivalent MySQL query. 
The database has a table called employees with the following columns: 
id, name, position, department, hire_date, salary. 

User Query: "{user_query}" 

Please provide ONLY the MySQL query, with no explanations or context.

"""

prod_db_url =os.getenv("PROD_DB_URL")

SECRET_KEY = os.getenv("PROD_DB_SECRET_KEY")