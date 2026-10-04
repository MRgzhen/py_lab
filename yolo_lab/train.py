from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
results = model.train(data="icon.yaml", workers=0, epochs=300, batch=8)
