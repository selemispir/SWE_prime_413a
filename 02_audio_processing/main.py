
import whisper

# Load the pretrained model
model = whisper.load_model("tiny")

# Get the audio file name
audio = input("Enter audio file name: ")

# Convert speech to text
result = model.transcribe(audio, fp16=False)

# Print the result
print("Transcription:", result["text"])
