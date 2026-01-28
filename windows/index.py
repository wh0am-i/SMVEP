import cv2
from ultralytics import YOLO

# Carrega o modelo (pode ser yolov8n.pt ou best.pt)
model = YOLO("../runs/detect/train/weights/best.pt")

# Abre o vídeo
cap = cv2.VideoCapture("F:/SMVEP/Videos/streetRioDia.mp4")  # caminho do vídeo

if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break  # fim do vídeo
    frame_up = cv2.resize(frame, (1280, 720))
    # Inferência
    results = model(frame_up, device=0, conf=0.7, half=True)
    print(len(results[0].boxes))

    # Desenha resultados
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"

            cv2.rectangle(frame_up, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame_up, label, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
            )

    cv2.imshow("YOLOv8 - Video", frame_up)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
