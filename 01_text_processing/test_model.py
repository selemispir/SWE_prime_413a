
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device="cpu"
)

sentences = [
    ("I love this movie.", "POSITIVE"),
    ("This food is terrible.", "NEGATIVE"),
    ("I am very happy.", "POSITIVE"),
    ("I hate this game.", "NEGATIVE"),
    ("The weather is beautiful.", "POSITIVE"),
    ("This is the worst day.", "NEGATIVE"),
    ("This book is amazing.", "POSITIVE"),
    ("I am disappointed.", "NEGATIVE"),
    ("The service was excellent.", "POSITIVE"),
    ("This is a bad idea.", "NEGATIVE")
]

correct = 0

for text, expected in sentences:
    result = classifier(text)[0]
    predicted = result["label"]

    print(text, "->", predicted)

    if predicted == expected:
        correct += 1

accuracy = correct / len(sentences) * 100

print("Accuracy:", round(accuracy, 2), "%")
