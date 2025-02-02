import re
from app.config import get_llm,sql_prompt

class NLPService:
    def __init__(self):
        self.llm = get_llm()

    def generate_sql_query(self, user_query: str) -> str:
        try:
            prompt = sql_prompt.format(user_query=user_query)
            sql_query = self.llm.invoke(prompt)

            sql_query = re.search(r"SELECT.*;", sql_query, re.DOTALL).group(0).strip()
            return sql_query
        except Exception as e:
            raise ValueError("Error Generating query:{e}")
