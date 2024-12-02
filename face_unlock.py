import face_recognition
import cv2
import pyautogui
import os
import time

# Load known faces
known_faces_dir = "known_faces"
known_faces = []
known_names = []

for filename in os.listdir(known_faces_dir):
    img = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
    encoding = face_recognition.face_encodings(img)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Camera error")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare detected face with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        if True in matches:
            print("Face recognized. Unlocking...")

            # Replace 'your_password' with your actual system password
            pyautogui.write('khaja12300')  
            pyautogui.press('enter')  # Simulate pressing Enter to unlock

            time.sleep(5)  # Wait for system to unlock
            break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
