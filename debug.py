#!/usr/bin/env python3
# debug.py
import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Get the API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Basic check for API key
if not OPENROUTER_API_KEY:
    print("Error: OPENROUTER_API_KEY not found in environment or .env file.")
    exit(1)

# 3. Correct the requests.post call syntax and header concatenation
r = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "deepseek/deepseek-chat-v3.1:free",
        "messages": [
            {
                "role": "user",
                "content": "hi"
            }
        ]
    }
)

print(f"Status Code: {r.status_code}")
print(f"Response Body: {r.text}")

# Optional: Parse and print JSON if successful
if r.status_code == 200:
    try:
        response_json = r.json()
        print("Model Response:", response_json['choices'][0]['message']['content'])
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
    except KeyError:
        print("Unexpected JSON structure in response.")