# settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()