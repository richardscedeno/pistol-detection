## Programa para detectar las armas con vision por computadora.
import cv2
import imutils
from ultralytics import YOLO
model = YOLO('../weights/best50.pt')


cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    frame_copy = frame.copy()
    frame_copy = imutils.resize(frame_copy, width=500)

    if success:
        results = model(frame, conf=0.8, save_crop=True)

        conf = results[0].boxes.conf
        # print(f'conf: {conf}')
        # print(type(conf))

        plot_frame = results[0].plot()

        cv2.imshow("YOLOv8", plot_frame)

        if conf.nelement() != 0:
            print(f'Tiene datos: {conf.nelement()}')
         #   funciones.validate_route()
        else:
            print(f'Está vacio: {conf.nelement()}')

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
