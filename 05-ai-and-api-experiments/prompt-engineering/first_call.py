import os
from openai import OpenAI

# The OpenAI library automatically looks for the OPENAI_API_KEY
# environment variable. If you've set it, you don't need to pass any arguments.
# Otherwise, you would pass it like this: client = OpenAI(api_key="YOUR_KEY")
client = OpenAI()

# Let's define our prompt using the RTCF framework
# This is where your prompt engineering skills come into play!
role_prompt = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
task_prompt = "Explain the concept of 'recursion' in programming."

print("Sending prompt to the AI...")

# This is the core API call.
# We specify the model we want to use and the messages we want to send.
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",  # A fast and capable model
  messages=[
    {"role": "system", "content": role_prompt},
    {"role": "user", "content": task_prompt}
  ]
)

# The API returns a complex object. The actual text response is nested inside.
ai_response_text = completion.choices[0].message.content

print("\n--- AI's Response ---")
print(ai_response_text)
print("---------------------\n")