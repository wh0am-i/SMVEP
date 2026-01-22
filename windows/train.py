from ultralytics import YOLO

def main():
    model = YOLO("../models/yolov8n.pt")

    model.train(
        data="../data.yaml",
        epochs=150,
        imgsz=640,
        batch=32,
        device=0
    )

if __name__ == "__main__":
    main()