from litellm import completion
import os

os.environ['DEEPSEEK_API_KEY'] = ""
os.environ['COHERE_API_KEY'] = ""

def main():
  response = completion(
      # model="deepseek/deepseek-chat", 
      model="command-r", 
      messages=[
        {"role": "user", "content": "hello from litellm"}
    ],
  )
  print(response)

if __name__ == "__main__":
    main()
