
from ultralytics import YOLO


model = YOLO("yolo11n.pt")


video = input("Enter video file name: ")



model.predict(
    source=video,
    save=True,
    conf=0.3,
    project="04_video_processing",
    name="results",
    exist_ok=True
)
