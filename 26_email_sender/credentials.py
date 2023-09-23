"""
IMPORTANT NOTE!

NEVER hardcode sensitive information into your scripts. You never know who
will get their hands on your script someday.

ALWAYS load sensitive from an external source that is not located in
your project.
"""

from os import getenv
from dotenv import load_dotenv, find_dotenv

# find the .env file and load it 
load_dotenv(find_dotenv())

from typing import Final

EMAIL: Final[str] = getenv("EMAIL_ADRESS")
PASSWORD: Final[str] = getenv("EMAIL_PASSWORD")
