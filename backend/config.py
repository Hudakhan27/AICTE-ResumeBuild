import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WKHTMLTOPDF_PATH = os.getenv("WKHTMLTOPDF_PATH")

# Optional debug print
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY[:5] + "...")
print("OPENAI_API_KEY:", OPENAI_API_KEY[:5] + "...")
print("WKHTMLTOPDF_PATH:", WKHTMLTOPDF_PATH)
