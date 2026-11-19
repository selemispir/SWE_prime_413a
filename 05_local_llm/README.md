
# Local LLM - Qwen3

## 1. Project Description
This project runs a large language model locally
on a computer using Ollama.

The model can answer questions and generate text.

## 2. Library
- Ollama
- Ollama Python library

## 3. Model
Qwen3 1.7B

Qwen3 is a pretrained language model.
It uses a Transformer-based architecture
to generate text.

I selected this model because it is small
and can run locally on my MacBook.

## 4. Input and Output
Input:
- Text questions

Output:
- AI-generated text answers

No training dataset is required for this project.
The model uses pretrained weights.

## 5. Model Evaluation
The model was tested with three questions:

1. What is Python?
2. What is machine learning?
3. What is artificial intelligence?

Evaluation metrics:
- Response time
- Answer relevance
- Answer quality

Observed response time:
- 2.91 seconds for one tested response

The answers can be manually reviewed
for correctness and relevance.

## 6. Implementation
The program:
1. Receives a question from the user.
2. Sends the question to the local model.
3. Generates an answer.
4. Displays the result.

No model training or fine-tuning is required.

## 7. How to Run

First, install Ollama from:
https://ollama.com

Download the model:

ollama pull qwen3:1.7b

Install the Python library:

pip install ollama

Run the application:

python 05_local_llm/main.py

Run the test:

python 05_local_llm/test_model.py

## 8. Conclusion
Qwen3 1.7B successfully generated answers
using a locally deployed language model.

The application does not require a
third-party AI inference service.
