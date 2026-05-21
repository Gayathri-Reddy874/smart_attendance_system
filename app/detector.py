import cv2


class FaceDetector:
    def __init__(self, model_path):
        self.net = cv2.dnn.readNetFromONNX(model_path)

    def detect(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255, (640, 640), swapRB=True)
        self.net.setInput(blob)
        outputs = self.net.forward()

        boxes = []

        for det in outputs[0]:
            x, y, w, h, conf = det[:5]

            if conf > 0.5:
                boxes.append((int(x), int(y), int(w), int(h), float(conf)))

        return boxes