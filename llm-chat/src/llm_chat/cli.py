from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY'] = ""
os.environ['COHERE_API_KEY'] = ""

def main():
  response = completion(
      # model="deepseek/deepseek-chat", 
      model="openai/gpt",
      api_key="sk-1234",
      api_base="http://127.0.0.1:3000",
      messages=[
        {"role": "user", "content": "hello from litellm"}
    ],
  )
  print(response)

if __name__ == "__main__":
    main()
