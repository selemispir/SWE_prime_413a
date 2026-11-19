
# Text Sentiment Analysis

## 1. Project Description
This project uses a pretrained machine learning model
to classify English text as positive or negative.

## 2. Library
- Hugging Face Transformers
- PyTorch

## 3. Model
DistilBERT (fine-tuned on SST-2)

The model analyzes text and predicts its sentiment.

## 4. Input and Output
Input: An English sentence.

Output:
- POSITIVE or NEGATIVE
- Confidence score

## 5. Model Evaluation
The model is tested using 10 English sentences.

Metric: Accuracy

Accuracy = Correct Predictions / Total Predictions

## 6. How to Run

Install the required libraries:

pip install "transformers[torch]"

Run the application:

python 01_text_processing/main.py

Run the test:

python 01_text_processing/test_model.py

## 7. Conclusion
This project demonstrates how to use a pretrained
machine learning model without training it from scratch.
