from promptflow import PromptFlow

# Initialize PromptFlow with a pre-trained model. 3.5 is way cheaper than 4!
model = PromptFlow(model_name="gpt-3.5-turbo")

# Generate text based on a prompt
prompt = "Translate the following English sentence into Chinese: 'Hello, how are you?'"
generated_text = model.generate(prompt)

print(generated_text)
