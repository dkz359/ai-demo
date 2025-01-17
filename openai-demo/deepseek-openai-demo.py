from openai import OpenAI
import os

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

print(response.choices[0].message.content)