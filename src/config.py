import os

from dotenv import load_dotenv

load_dotenv("/Users/jacob/github.com/jda5/stance-evals/.env")

OPENAI_KEY = os.getenv("OPENAI_KEY")
