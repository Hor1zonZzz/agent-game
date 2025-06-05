# Forbidden Change: This code patches the OpenAI class to print total tokens used in chat completions.
import openai


original_openai_class = openai.OpenAI


# 定义一个新的类，继承自 OpenAI，并修改它的 .chat.completions.create
class PatchedOpenAI(openai.OpenAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        original_create = self.chat.completions.create

        def wrapped(*a, **kw):
            result = original_create(*a, **kw)
            print("=======>total tokens: ", result.usage.total_tokens)
            return result

        self.chat.completions.create = wrapped


# 替换全局 openai.OpenAI
openai.OpenAI = PatchedOpenAI


# Your agent code here
# Following is an example of a simple agent that uses OpenAI's API to answer questions.
# Currently, Just Supports OpenAI SDK


import sys

# This is a simple agent that reads a task from the command line arguments
task = sys.argv[1]
print(f"Received task: {task}")


client = openai.OpenAI(
    api_key="sk-xxxxxxxxx",
    base_url="https://openrouter.ai/api/v1",
)
resp = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)
print(resp.choices[0].message.content)

