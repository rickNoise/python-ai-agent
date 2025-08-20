import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    
    if len(sys.argv) < 2:
        print("usage: python main.py \"<LLM PROMPT>\"")
        sys.exit(1)
    user_prompt = sys.argv[1]
    user_flags = sys.argv[2:]

    verboseResponse = "--verbose" in user_flags

    api_key = os.environ.get("GEMINI_API_KEY")
    # create a new instance of a Gemini client
    # https://googleapis.github.io/python-genai/#create-a-client
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    call_LLM(client, messages, user_prompt, verboseResponse)


def call_LLM(client, messages, user_prompt="", verboseResponse=False):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )

    print("Response:")
    print(response.text)

    if verboseResponse:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
