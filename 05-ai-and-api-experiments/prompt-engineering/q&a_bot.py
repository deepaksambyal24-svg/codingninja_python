import os
from openai import OpenAI

# --- 1. Setup: Initialize the Client ---
# The client will automatically use the OPENAI_API_KEY environment variable.
# We're adding a retry mechanism for resilience, as discussed in 4.8.
try:
    client = OpenAI(max_retries=2)
except TypeError:
    # Fallback for older versions of the openai library
    client = OpenAI()

# --- 2. Prompt Engineering: Define the Persona ---
# This is our powerful System Prompt, as discussed in 4.5.
# It sets the rules and personality for our bot for the entire session.
SYSTEM_PROMPT = """
You are 'History Helper,' a friendly and knowledgeable assistant specializing in history.
Your goal is to answer user questions accurately and engagingly.
- Your tone should be like a passionate history teacher.
- When you mention a date, always include the year.
- If you don't know the answer to a question, you must say "That's a fascinating question, but it's outside my area of historical expertise."
"""

# We will store the conversation history to maintain context.
conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("--- History Helper Bot ---")
print("Ask me any history question! Type 'exit' to end the chat.")

# --- 3. The Main Application Loop ---
while True:
    # Get input from the user
    user_input = input("\nYou: ")

    # Check for exit condition
    if user_input.lower() == 'exit':
        print("Farewell! May your future be as interesting as the past.")
        break

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    try:
        # --- 4. The API Call with Streaming ---
        # We set `stream=True` to get the response back token-by-token.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            stream=True,  # This is the key to real-time chat!
        )

        print("History Helper: ", end="")
        ai_response_content = ""
        # Loop through the chunks of the streamed response
        for chunk in stream:
            # Check if there is content in the chunk
            if chunk.choices[0].delta.content is not None:
                chunk_text = chunk.choices[0].delta.content
                ai_response_content += chunk_text
                print(chunk_text, end="", flush=True)

        # Add a newline after the full response is printed
        print()

        # Add the AI's complete response to the history for context in the next turn
        conversation_history.append({"role": "assistant", "content": ai_response_content})

    except Exception as e:
        # --- 5. Error Handling ---
        print(f"\nAn error occurred: {e}")
        # Remove the last user message from history so we can retry
        conversation_history.pop()