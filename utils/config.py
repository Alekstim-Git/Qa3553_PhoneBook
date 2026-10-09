from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

BASE_URL = getenv("BASE_URL")
EXISTING_USER_EMAIL = getenv("EXISTING_USER_EMAIL")
EXISTING_USER_PASSWORD = getenv("EXISTING_USER_PASSWORD")
