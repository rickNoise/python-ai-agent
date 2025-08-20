import os, sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    
    if len(sys.argv) < 2:
        print("usage: python main.py \"<LLM PROMPT>\"")
        sys.exit(1)
    user_prompt = sys.argv[1]

    api_key = os.environ.get("GEMINI_API_KEY")
    # create a new instance of a Gemini client
    # https://googleapis.github.io/python-genai/#create-a-client
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=user_prompt,
    )

    print("Response:")
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
