import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.db")

settings = Settings()
