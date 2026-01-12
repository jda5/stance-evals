import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv

ROOT = dirname(dirname(abspath(__file__)))

load_dotenv(join(ROOT, ".env"))


ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")
