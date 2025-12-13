import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`


print(args)
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("INVALID API KEY")

client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

res = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if res.usage_metadata is not None and args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

print(res.text)
