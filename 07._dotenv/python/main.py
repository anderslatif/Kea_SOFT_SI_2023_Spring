# Example 1
from dotenv import load_dotenv, dotenv_values
dotenv_values = dotenv_values()
print(dotenv_values.get("MY_SECRET"))

# Example 2
load_dotenv()
import os
print(os.getenv("MY_SECRET"))

