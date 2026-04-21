#!/usr/bin/env python3
# deepseek_request.py
# Prints full HTTP response text when status != 2xx so 
# you can see error message JSON from OpenRouter

import os, sys, requests, json

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    print("Error: set OPENROUTER_API_KEY in the environment (PowerShell: $env:OPENROUTER_API_KEY = 'sk-...')", file=sys.stderr)
    sys.exit(1)

url = "https://openrouter.ai/api/v1/chat/completions"
payload = {
    "model": "deepseek/deepseek-chat-v3.1:free",
    "messages": [{"role": "user", "content": "Can you provide me with some PowerShell snippets that I can use?"}]
}
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

try:
    resp = requests.post(url, json=payload, headers=headers, timeout=20)
except requests.exceptions.RequestException as e:
    print("Network/connection error:", e, file=sys.stderr)
    sys.exit(2)

# Print status + raw body so we can see any error info from the server
print("HTTP", resp.status_code)
print(resp.text)

# If it's JSON and success, pretty print it
if resp.headers.get("Content-Type", "").startswith("application/json") and resp.ok:
    print(json.dumps(resp.json(), indent=2))
