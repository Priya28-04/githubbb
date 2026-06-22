from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Extract variables
database_url = os.getenv("DATABASE_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
secret_key = os.getenv("SECRET_KEY")
debug = os.getenv("DEBUG")
port = os.getenv("PORT")
email = os.getenv("EMAIL")

# Print values
print("Database URL:", database_url)
print("Username:", username)
print("Password:", password)
print("Secret Key:", secret_key)
print("Debug Mode:", debug)
print("Port:", port)
print("Email:", email)


import os
from dotenv import load_dotenv

# --- Load the .env file FIRST ---
# This line finds the '.env' file in your project root,
# reads it, and populates os.environ.
# If you don't call this, os.getenv will return None for .env variables.
load_dotenv()

# --- Use os.getenv() for safe access ---
# Option A: Safe method. Returns None if variable is missing.
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

# Option B: Safe method with a default fallback value.
# This is excellent for optional configs.
debug_mode = os.getenv("DEBUG_MODE", "False") # Defaults to 'False' if not found
port = os.getenv("PORT", "8000") # Default to 8000 if PORT not set

# Option C (DANGEROUS): Using os.environ["KEY"] directly.
# This will crash your program with a KeyError if the variable is missing.
# Only use this if you are 100% sure the variable is set and the program
# MUST NOT run without it.
# api_key = os.environ["API_KEY"]  #.Not recommended

# --- Always validate critical variables ---
# This is what separates a junior dev script from production code.
if not database_url:
    # Instead of a cryptic error deep in the code, you fail fast with a clear message.
    raise ValueError("FATAL ERROR: DATABASE_URL is not set. Check your .env file.")

if not secret_key:
    raise ValueError("FATAL ERROR: SECRET_KEY is not set. Check your .env file.")

# --- Simulate the connection logic ---
print(f"--- App Configuration ---")
print(f"DEBUG MODE: {debug_mode}")
print(f"PORT: {port}")
print(f"Attempting to connect to the database...")
# Pretend we are using the URL, but we'll just print a masked version for safety.
# NEVER print your full database URL or secret key in a real log!
if database_url:
    # Simple masking: show first 20 chars only
    print(f"Using Database URL: {database_url[:20]}...")
    print("Connection successful! (Simulated)")
else:
    print("Connection failed.")

print(f"Secret key loaded successfully (length: {len(secret_key)} characters).")