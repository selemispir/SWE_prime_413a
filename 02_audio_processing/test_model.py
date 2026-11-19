
import whisper
from jiwer import wer

# Load the model
model = whisper.load_model("tiny")

# Correct text
reference = "And so my fellow Americans ask not what your country can do for you ask what you can do for your country"

# Convert audio to text
result = model.transcribe(
    "02_audio_processing/jfk.flac",
    fp16=False
)

prediction = result["text"]

# Remove punctuation and make lowercase
reference = reference.lower().replace(".", "").replace(",", "")
prediction = prediction.lower().replace(".", "").replace(",", "")

# Calculate error
error = wer(reference, prediction)

print("Whisper result:", prediction)
print("Word Error Rate:", round(error * 100, 2), "%")
