import os

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ API Key Found")
    print(api_key[:12] + "...")
else:
    print("❌ API Key Not Found")