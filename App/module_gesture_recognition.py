import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2

# Load mô hình nhận diện cử chỉ tay
model_path = r'D:\Project\HandGesture_Community_Edition\models\my_model.keras'
try:
    model = keras.models.load_model(model_path, compile=False)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Danh sách nhãn của mô hình
labels = ['thumb', 'fist', 'open_hand']

def predict_gesture(image):
    if model is None:
        return "Unknown"
    
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Đảm bảo là ảnh RGB
        image = cv2.resize(image, (256, 256))  # ✅ Resize đúng kích thước model yêu cầu
        image = np.expand_dims(image, axis=0) / 255.0  # Chuẩn hóa dữ liệu
        prediction = model.predict(image, verbose=0)[0]
        return labels[np.argmax(prediction)]
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return "Unknown"
