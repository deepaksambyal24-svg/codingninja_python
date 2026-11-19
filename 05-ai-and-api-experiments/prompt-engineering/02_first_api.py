from openai import OpenAI

# Create the OpenAI client
client = OpenAI()

# Send a prompt to GPT
response = client.responses.create(
    model="gpt-4.1",
    input="Hello! Introduce yourself in two sentences."
)

# Print GPT's reply
print(response.output_text)