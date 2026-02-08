# app/routes/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from PIL import Image
import io
import tensorflow as tf
import numpy as np
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"   # Add this line at the very top

# Now import tensorflow
# ... rest of your code

router = APIRouter(prefix="/upload", tags=["Upload & Prediction"])

# Load model only once when the module imports
# We use os.getcwd() to ensure we are looking relative to the project root (E:\brain-tumor-project)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Should reach project root
MODEL_PATH = os.path.join(BASE_DIR, "app", "models", "Brain_Tumor_Model.h5")

print(f"Attempting to load model from: {MODEL_PATH}")

try:
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully!")
    else:
        print(f"CRITICAL ERROR: Model file not found at: {MODEL_PATH}")
        print(f"Current working directory: {os.getcwd()}")
        model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@router.get("/mri/")
async def main():
    model_status = "✅ Model Loaded" if model is not None else "❌ Model Not Loaded (Check Console)"
    model_color = "green" if model is not None else "red"
    
    content = f"""
<body>
<h2>Upload MRI Image</h2>
<p style="color: {model_color}; font-weight: bold;">{model_status}</p>
<form action="/upload/mri/" enctype="multipart/form-data" method="post">
<input name="file" type="file" accept=".jpg,.jpeg,.png">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@router.post("/mri/")
async def predict_mri(file: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Check server logs.")

    print(f"Received file: {file.filename}") # Debugging print

    # Specific check for common user error (uploading the model instead of an image)
    if file.filename.lower().endswith('.h5'):
        raise HTTPException(
            status_code=400, 
            detail="You are uploading the AI Model file (.h5). You must upload a PATIENT IMAGE (jpg/png) to test the model."
        )

    # Check file type
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid file type: '{file.filename}'. Only JPG/PNG images are allowed."
        )

    try:
        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")
        
        # Resize to match your model's input size
        # ERROR FIX: Model expects (224, 224), was previously (150, 150)
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0          # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict
        prediction = model.predict(img_array)[0][0]   # Assuming binary output
        
        # For binary classification (tumor / no tumor)
        if prediction > 0.5:
            result = "Tumor Detected"
            confidence = round(float(prediction) * 100, 2)
        else:
            result = "No Tumor Detected"
            confidence = round((1 - float(prediction)) * 100, 2)

        # If your model is multi-class (e.g., glioma, meningioma, pituitary, no tumor)
        # Replace above with:
        # class_names = ['glioma', 'meningioma', 'pituitary', 'no tumor']
        # predicted_class = class_names[np.argmax(prediction)]
        # confidence = round(float(np.max(prediction)) * 100, 2)
        # result = f"{predicted_class} ({confidence}%)"

        return JSONResponse({
            "result": result,
            "confidence": f"{confidence}%",
            "filename": file.filename
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")