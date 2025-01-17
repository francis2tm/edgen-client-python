#!/usr/bin/env -S poetry run python

from edgen import Edgen

client = Edgen()

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="zephyr-7b-beta.Q4_K_M.gguf",
    messages=[
        {
            "role": "user",
            "content": "what is 1 + 2?",
        },
    ],
)

# print(completion.choices[0].delta.content)
print(completion)

"""
# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="zephyr-7b-beta.Q4_K_M.gguf",
    messages=[
        {
            "role": "user",
            "content": "recite Stopping by Woods on a Snowy Evening",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()
"""
