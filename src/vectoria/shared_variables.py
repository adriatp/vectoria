from dotenv import load_dotenv
import os

# Update environment vars
load_dotenv()

# Configuration IMAP
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_PORT = os.getenv("IMAP_PORT")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
KEYWORD = os.getenv("KEYWORD")