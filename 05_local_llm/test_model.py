
from ollama import chat
import time

questions = [
    "What is Python?",
    "What is machine learning?",
    "What is artificial intelligence?"
]

for question in questions:
    start = time.time()

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {"role": "user", "content": question}
        ],
        think=False
    )

    end = time.time()

    print("Question:", question)
    print("Answer:", response.message.content)
    print("Time:", round(end - start, 2), "seconds")
    print("--------------------")

from ollama import chat
import time

questions = [
    "What is Python?",
    "What is machine learning?",
    "What is artificial intelligence?"
]

for question in questions:
    start = time.time()

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {"role": "user", "content": question}
        ],
        think=False
    )

    end = time.time()

    print("Question:", question)
    print("Answer:", response.message.content)
    print("Time:", round(end - start, 2), "seconds")
    print("--------------------")
