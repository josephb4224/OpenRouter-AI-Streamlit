#!/usr/bin/env python3

# Debug the OpenRouter AI requests:
# Model: Deepseek

$env:OPENROUTER_API_KEY="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"

import os
import requests,json

r=requests.post(
    "https://openrouter.ai/api/v1/chat/completions"

    headers={
        "Authorization":"Bearer ",
        +os.getenv( "OPENROUTER_API_KEY", "" ),
        "Content-Type":"application/json"
    }

    json={
        "model":"deepseek/deepseek-chat-v3.1:free",
        "messages":[
            {
                "role":"user",
                "content":"hi"
            }
        ]
    }
)

print(r.status_code)
print(r.text)
