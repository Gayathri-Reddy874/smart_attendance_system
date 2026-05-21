# 🎯 AI-Based Smart Attendance System Using Face Recognition

An intelligent attendance management system that automates attendance using **Artificial Intelligence, Computer Vision, and Face Recognition Technology**. The system detects and recognizes faces in real time using a webcam and automatically marks attendance in a MySQL database.

It also provides:
- 📧 Automated Email Notifications
- 📊 Attendance Analytics Dashboard
- 🔒 Duplicate Attendance Prevention
- ⚡ Real-Time Face Recognition

---

# 📌 Introduction

Traditional attendance methods such as manual registers, RFID cards, or fingerprint systems are time-consuming and prone to proxy attendance and human errors.

This project uses:
- **OpenCV**
- **YOLOv8 Face Detection**
- **Deep Learning**
- **MySQL**
- **Streamlit**

to automate attendance management efficiently and securely.

---

# 🎯 Objectives

- Automate attendance using facial recognition
- Eliminate proxy attendance
- Provide real-time face detection & recognition
- Store attendance securely in a database
- Generate attendance analytics
- Send automated email notifications

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| OpenCV | Image Processing |
| YOLOv8 ONNX Model | Face Detection |
| NumPy | Numerical Computation |
| Pickle | Face Embedding Storage |
| MySQL | Attendance Database |
| Streamlit | Dashboard Interface |
| Deep SORT | Face Tracking |
| SMTP | Email Notification System |

---

# 📂 Project Structure

```bash
Smart-Attendance-System/
│
├── app/
│   ├── main.py
│   └── register_face.py
│
├── embeddings/
│   └── create_embeddings.py
│
├── dataset/
│
├── models/
│
├── streamlit_app/
│   └── dashboard.py
│
├── database/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Gayathri-Reddy874/smart_attendance_system.git
cd Smart-Attendance-System
```

---

## 2️⃣ Check Folder Path

Make sure you are inside the project folder.

```bash
cd foldername
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv env
```

---

## 4️⃣ Activate Environment

### Windows

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
source env/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📸 Face Registration

To register new faces:

```bash
python app/register_face.py
```

### Features
- Automatic image capture
- Dataset creation
- Person-wise image storage

---

# 🧠 Create Face Embeddings

To create embeddings and generate `.pkl` file:

```bash
python embeddings/create_embeddings.py
```

### Features
- Face preprocessing
- Feature extraction
- Embedding storage

---

# 🚀 Run Attendance System

```bash
python -m app.main
```

### Features
- Real-time face detection
- Face recognition
- Automatic attendance marking
- Duplicate prevention
- Email notification support

---

# 📊 Run Dashboard

```bash
streamlit run streamlit_app/dashboard.py
```

### Dashboard Features
- Attendance analytics
- Daily trends
- Person-wise attendance count
- Real-time attendance records

---

# 🧩 System Modules

## 1. Face Registration Module
Captures multiple face images and stores them in dataset folders.

## 2. Embedding Creation Module
Converts face images into numerical embeddings for recognition.

## 3. Face Detection Module
Uses YOLOv8 ONNX model for detecting faces from webcam frames.

## 4. Face Recognition Module
Matches detected faces with stored embeddings using Euclidean distance.

## 5. Attendance Management Module
Stores attendance records with date and time in MySQL database.

## 6. Email Alert Module
Sends automated email notifications after attendance marking.

## 7. Dashboard Module
Displays attendance analytics and reports using Streamlit.

---

# 🔄 Working Principle

1. Register face images using webcam
2. Create facial embeddings
3. Webcam captures live video
4. YOLOv8 detects faces
5. System recognizes faces
6. Attendance gets marked automatically
7. Email alert is sent
8. Dashboard displays attendance statistics

---

# 🗄️ Database Design

## Table: attendance_new

| Field Name | Type |
|------------|------|
| id | Integer |
| name | Varchar |
| time | Time |
| date | Date |

---

# ✅ Advantages

- Fully automated attendance system
- Eliminates proxy attendance
- Fast and accurate recognition
- Real-time monitoring
- Easy record management
- Secure data storage
- Email notification support

---

# 📚 Applications

- Colleges & Universities
- Schools
- Offices & Companies
- Training Institutes
- Smart Classrooms
- Employee Monitoring Systems

---

# 🚀 Future Enhancements

- Cloud database integration
- Mobile application support
- Multi-camera support
- Mask face recognition
- PDF/Excel attendance export
- Anti-spoofing detection
- AI-based analytics

---

# 📌 Conclusion

The AI-Based Smart Attendance System provides a smart, secure, and automated solution for attendance management using Face Recognition and Artificial Intelligence. By integrating Computer Vision, Deep Learning, and Database Management, the system improves accuracy, reduces manual effort, and enables efficient attendance tracking.

---

# 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

# 👩‍💻 Author

**Mallareddygari Gayathri**

- GitHub: https://github.com/Gayathri-Reddy874
```
