
from transformers import pipeline

# Load the pretrained model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device="cpu"
)

# Ask the user to enter a sentence
text = input("Enter an English sentence: ")

# Analyze the sentence
result = classifier(text)[0]

# Print the result
print("Sentiment:", result["label"])
print("Confidence:", round(result["score"] * 100, 2), "%")
