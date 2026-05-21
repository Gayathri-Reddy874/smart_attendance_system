import cv2
import numpy as np
import pickle
from config import FACE_THRESHOLD


class FaceRecognizer:
    def __init__(self, embedding_path):
        with open(embedding_path, "rb") as f:
            self.known_faces = pickle.load(f)

    def get_embedding(self, face_img):
        face = cv2.resize(face_img, (160, 160))
        face = face.astype("float32") / 255.0
        return face.flatten()

    def recognize(self, face_img):

        try:
            input_emb = self.get_embedding(face_img)
        except:
            return "Unknown"

        best_match = "Unknown"
        min_distance = float("inf")

        for name, emb_list in self.known_faces.items():
            for db_emb in emb_list:
                dist = np.linalg.norm(input_emb - db_emb)

                if dist < min_distance:
                    min_distance = dist
                    best_match = name

        return best_match if min_distance < FACE_THRESHOLD else "Unknown"