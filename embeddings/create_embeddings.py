import os
import cv2
import numpy as np
import pickle

dataset_path = "dataset"
embeddings = {}

def get_embedding(img):
    img = cv2.resize(img, (160, 160))
    img = img.astype("float32") / 255.0
    return img.flatten()  # full vector (better than slicing)

for person in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person)

    if not os.path.isdir(person_folder):
        continue

    embeddings[person] = []

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)

        img = cv2.imread(img_path)
        if img is None:
            continue

        emb = get_embedding(img)
        embeddings[person].append(emb)

print("Saving embeddings...")

os.makedirs("embeddings", exist_ok=True)

with open("embeddings/faces.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("✅ faces.pkl created successfully")