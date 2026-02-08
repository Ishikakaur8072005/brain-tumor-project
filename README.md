# 🧠 Brain Tumor Detection System

A full-stack web application designed to assist in the early detection of brain tumors using MRI imagery and Deep Learning. This system integrates a **React** frontend for an intuitive user experience with a **FastAPI** backend for robust and efficient model serving.

![Project Status](https://img.shields.io/badge/Status-Development-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🚀 Features

-   **MRI Image Analysis**: Upload MRI scans to detect the presence of brain tumors (Glioma, Meningioma, Pituitary).
-   **Interactive Dashboard**: Visualizes global health trends and statistics.
-   **User Analytics**: Tracks user demographics and scan history (Privacy-focused).
-   **Responsive Design**: Modern UI built with React and custom CSS.

## 🛠️ Tech Stack

### Frontend
-   **React.js**: Component-based UI library.
-   **React Router**: For seamless single-page navigation.
-   **Leaflet Maps**: Interactive maps for geographical data visualization.

### Backend
-   **FastAPI**: High-performance, easy-to-learn web framework for building APIs with Python.
-   **TensorFlow/Keras**: Deep learning framework for the classification model.
-   **Pillow**: Python Imaging Library for image processing.
-   **NewsAPI**: For fetching global health news and trends.

## 📦 Installation & Setup

### Prerequisites
-   Node.js (v14+)
-   Python (v3.8+)

### 1. Clone the Repository
```bash
git clone https://github.com/Ishikakaur8072005/brain-tumor-project.git
cd brain_tumor_project
```

### 2. Backend Setup
Navigate to the backend directory and install dependencies:
```bash
cd brain-tumor-backend
pip install -r requirements.txt
```

> **⚠️ Important**: You must place your trained model file `Brain_Tumor_Model.h5` in the `brain-tumor-backend/app/models/` directory for predictions to work.

Start the Backend Server:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

### 3. Frontend Setup
Open a new terminal, navigate to the frontend directory, and install dependencies:
```bash
cd brain-tumor-frontend
npm install
```

Start the Frontend Application:
```bash
npm start
```
The application will run at `http://localhost:3000`.

## 🗺️ Roadmap

- [ ] Integration of advanced segmentation models.
- [ ] User authentication and secure history storage.
- [ ] Docker containerization for easy deployment.
- [ ] CI/CD Pipeline integration.


