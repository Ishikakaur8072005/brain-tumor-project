# 🧠 Brain Tumor Detection System

A machine learning-powered web application for detecting and classifying brain tumors from MRI scans using deep learning.

## 📋 Features

- **MRI Image Upload & Analysis**: Upload brain MRI scans for automated tumor detection
- **Deep Learning Classification**: Powered by TensorFlow/Keras for accurate predictions
- **RESTful API**: FastAPI-based backend for seamless integration
- **Analytics Dashboard**: Track predictions and trends over time
- **Real-time Processing**: Fast and efficient image processing pipeline

## 🚀 Technologies Used

- **Backend**: FastAPI
- **Machine Learning**: TensorFlow, Keras
- **Image Processing**: Pillow
- **Database**: PostgreSQL (optional)
- **Environment Management**: Python dotenv

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Praveen23-kk/brain-tumor-project.git
cd brain-tumor-project
```

2. **Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory with your configuration.

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

Once the server is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 🔍 Usage

1. Navigate to `/docs` endpoint
2. Use the `/upload/mri/` endpoint to upload MRI images
3. Receive predictions and classification results
4. View analytics and trends through the analytics endpoints

## 📁 Project Structure

```
brain-tumor-project/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── routes/           # API route handlers
│   ├── models/           # ML models
│   └── utils/            # Utility functions
├── data/                 # Data storage
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not tracked)
└── README.md            # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**K Praveen Kumar**
- GitHub: [@Praveen23-kk](https://github.com/Praveen23-kk)

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Always consult with qualified medical professionals for medical diagnoses.
