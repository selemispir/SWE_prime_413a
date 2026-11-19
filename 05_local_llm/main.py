
from ollama import chat


question = input("Ask a question: ")


response = chat(
    model="qwen3:1.7b",
    messages=[
        {"role": "user", "content": question}
    ],
    think=False
)


print("\nAI Answer:")
print(response.message.content)
