import cv2
import os
import time

name = input("Enter person name: ")

save_path = f"dataset/{name}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
max_images = 20   # number of images to capture

print("📸 Auto capturing images... Look at camera")

start_time = time.time()

while count < max_images:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working ❌")
        break

    cv2.imshow("Register Face", frame)

    # capture every 1 second
    if time.time() - start_time > 1:
        img_path = f"{save_path}/{count}.jpg"
        cv2.imwrite(img_path, frame)
        print(f"Saved {img_path}")
        count += 1
        start_time = time.time()

    # just for display refresh (no key dependency)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

print("✅ Dataset created successfully")