# Your agent code here

import sys
from litellm import completion
import os

## set ENV variables
os.environ["OPENROUTER_API_KEY"] = "sk-xxxxxxxx"


response = completion(
    model="openrouter/openai/gpt-4o-mini",
    messages=[{ "content": "hi","role": "user"}]
)

print(response)

task = sys.argv[1]

print(task)
