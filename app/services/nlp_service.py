# backend/app/services/nlp_service.py

from dotenv import load_dotenv
import os
import re
from langchain_huggingface.llms import HuggingFaceEndpoint

# Load environment variables
load_dotenv()

class NLPService:
    def __init__(self):
        # Get the API key from environment variables
        self.huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not self.huggingface_api_key:
            raise ValueError("Hugging Face API key not found in .env file.")

        # Define the Hugging Face repository and LLM endpoint configuration
        self.repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
        self.llm = HuggingFaceEndpoint(
            repo_id=self.repo_id,
            temperature=0.7,
            max_new_tokens=500,
            model_kwargs={"token": self.huggingface_api_key}  # Pass token here
        )

    def generate_sql_query(self, user_query: str) -> str:
        """
        Converts a natural language query into an SQL query using the Hugging Face model.
        """
        try:
            # Generate an SQL query using the LLM
            sql_query = self.llm.invoke(
                f"Convert the following user query into an equivalent MySQL query. The database has a table called employees with the following columns: id, name, position, department, hire_date, salary. \n\nUser Query: \"{user_query}\" \n\nPlease provide ONLY the MySQL query, with no explanations or context."
            )
            
            # Extract only the SQL query from the output
            sql_query = re.search(r"SELECT.*;", sql_query, re.DOTALL).group(0).strip()
            return sql_query
        except Exception as e:
            raise ValueError(f"Error generating SQL query: {e}")