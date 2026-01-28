from ultralytics import YOLO

def main():

    # Treinamento
    model = YOLO("../models/yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=1280,
        rect=True,
        device=0,

        cache="disk",
        workers=6,
        batch=6,
        amp=False,
        deterministic=False
    )

if __name__ == "__main__":
    main()
