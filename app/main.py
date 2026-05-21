import cv2

from app.detector import FaceDetector
from app.recognizer import FaceRecognizer
from app.attendance_logic import mark_attendance


detector = FaceDetector("models/yolov8-face.onnx")
recognizer = FaceRecognizer("embeddings/faces.pkl")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    boxes = detector.detect(frame)

    for (x, y, w, h, conf) in boxes:
        face = frame[y:y+h, x:x+w]

        name = recognizer.recognize(face)

        if name and name != "Unknown":
            mark_attendance(name)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()