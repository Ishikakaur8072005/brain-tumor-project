from fastapi import FastAPI
from app.routes import upload, trends, analytics 
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"   # Add this line at the very top

# Now import tensorflow
import tensorflow as tf
# ... rest of your code# Make sure upload is imported
from silence_tensorflow import silence_tensorflow
silence_tensorflow()

app = FastAPI(title="Brain Tumor Detection API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(upload.router)       # This connects the upload endpoints
app.include_router(trends.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs to test uploads and predictions."}