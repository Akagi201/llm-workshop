from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://127.0.0.1:3000/v1",
)

completion = client.chat.completions.create(
    model="pai-001",
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant that speaks Chinese.",
        },
        {"role": "user", "content": "Hello, from 0g user!"},
    ],
    temperature=0.9,
)

print(completion.choices[0].message)
