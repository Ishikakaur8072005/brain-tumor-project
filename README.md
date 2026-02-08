# Brain Tumor Detection System

A full-stack web application designed to assist in the early detection of brain tumors using MRI imagery and Deep Learning. This system integrates a React frontend for an intuitive user experience with a FastAPI backend for robust and efficient model serving.

![Project Status](https://img.shields.io/badge/Status-Development-orange)

## Features

-   **MRI Image Analysis**: Upload MRI scans to detect the presence of brain tumors (Glioma, Meningioma, Pituitary).
-   **Interactive Dashboard**: Visualizes global health trends and statistics.
-   **User Analytics**: Tracks user demographics and scan history (Privacy-focused).
-   **Responsive Design**: Modern UI built with React and custom CSS.

## Tech Stack

### Frontend
-   **React.js**: Component-based UI library.
-   **React Router**: For seamless single-page navigation.
-   **Leaflet Maps**: Interactive maps for geographical data visualization.

### Backend
-   **FastAPI**: High-performance, easy-to-learn web framework for building APIs with Python.
-   **TensorFlow/Keras**: Deep learning framework for the classification model.
-   **Pillow**: Python Imaging Library for image processing.
-   **NewsAPI**: For fetching global health news and trends.

## Installation & Setup Guide

Follow these steps to set up the project locally.

### Prerequisites
-   **Node.js** (v14 or higher): Required for the frontend.
-   **Python** (v3.8 or higher): Required for the backend.
-   **Git**: For cloning the repository.

### 1. Clone the Repository

Open your terminal or command prompt and run the following command to download the code:

```bash
git clone https://github.com/Ishikakaur8072005/brain-tumor-project.git
cd brain_tumor_project
```

### 2. Backend Setup

The backend handles the AI model and API requests.

1.  Navigate to the backend directory:
    ```bash
    cd brain-tumor-backend
    ```

2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Critical Step**: Add the Model File
    -   You must obtain the trained model file named `Brain_Tumor_Model.h5`.
    -   Place this file inside the `brain-tumor-backend/app/models/` directory.
    -   If this file is missing, the application will start but prediction features will fail.

4.  Start the Backend Server:
    ```bash
    uvicorn app.main:app --reload
    ```
    You should see a message indicating the server is running at `http://127.0.0.1:8000`.

### 3. Frontend Setup

The frontend is the user interface you interact with in your browser.

1.  Open a **new** terminal window (keep the backend running in the first one).

2.  Navigate to the frontend directory:
    ```bash
    cd brain_tumor_project/brain-tumor-frontend
    ```

3.  Install the required JavaScript packages:
    ```bash
    npm install
    ```

4.  Start the Frontend Application:
    ```bash
    npm start
    ```
    This will automatically open your web browser to `http://localhost:3000`.

## How to Use

1.  **Dashboard**: View global trends and latest health news related to brain tumors.
2.  **Upload MRI**: Navigate to the upload section. Click "Choose File" to select an MRI image (.jpg, .png) from your computer. Click "Analyze" to get a prediction.
3.  **Analytics**: View your session statistics and location-based data.

## Roadmap

- Integration of advanced segmentation models.
- User authentication and secure history storage.
- Docker containerization for easy deployment.
- CI/CD Pipeline integration.
