# Install the OpenAI package
# pip install openai
'''
import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Chatbot query
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 ideas that I could build using OpenAI APIs"}
    ]
)

# Print response
print(completion.choices[0].message.content)
'''
# Simple Chatbot using OpenAI (for openai >= 1.0.0)
from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 project ideas using OpenAI APIs"}
    ]
)

print(response.choices[0].message.content)
