import os
import random
import anthropic

# Setup Claude client
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
if not CLAUDE_API_KEY:
    raise ValueError("Please set CLAUDE_API_KEY as a pipeline secret variable.")

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)


# Read last 30 lines from build/test log
log_file = "test_output.log"
if not os.path.exists(log_file):
    print(f"Log file '{log_file}' not found!")
    exit(1)

print("\n--- Log File ---\n")

with open(log_file, "r") as f:
    log_tail = "".join(f.readlines()[-30:])  # last 30 lines
    print(log_tail)


# Prepare the prompt
prompt = (
    "You are a DevOps assistant.\n"
    "Explain the following build failure clearly and suggest a fix.\n"
    "Respond in a professional way suitable for a CI/CD pipeline report.\n\n"
    f"Error logs:\n{log_tail}"
)


# Call Claude API
try:
    response = client.messages.create(
        model="claude-opus-4-1-20250805", #"claude-3-5-sonnet-20241022",
        max_tokens=300,
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    print("\n====== LLM Response ======")
    print(response)
    print("==========================")

    text = response.content[0].text.strip()

    print("\n--- Claude Build Failure Analysis ---\n")
    print(text)
    print("\n------------------------------------\n")

except Exception as e:
    print(f"[Error] Claude API call failed: {e}")
