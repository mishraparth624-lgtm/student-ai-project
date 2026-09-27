import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

topic = input("Enter a topic: ")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"Explain {topic} in simple terms for a 2nd-year computer science student."
)

print("\nGemini Response:\n")
print(response.text)