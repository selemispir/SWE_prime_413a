
from ultralytics import YOLO


model = YOLO("yolo11n.pt")


video = "04_video_processing/test_video.mp4"


results = model.predict(source=video, conf=0.3, verbose=False)

total = 0

for frame in results:
    total += len(frame.boxes)

print("Total detections:", total)
print("Frames processed:", len(results))
print("Test completed!")
