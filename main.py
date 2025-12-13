import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("INVALID API KEY")

client = genai.Client(api_key=api_key)

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
)

if res.usage_metadata is not None:
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

print(res.text)
