from ultralytics import YOLO

def main():

    # Treinamento
    model = YOLO("../models/yolo11x.pt")

    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=896,
        rect=True,
        device=0,

        cache="disk",
        workers=6,
        batch=2,
        amp=False,
        deterministic=False
    )

if __name__ == "__main__":
    main()
