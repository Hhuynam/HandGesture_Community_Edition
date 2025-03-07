import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Đường dẫn tới mô hình đã huấn luyện
model_path = r"D:\Project\HandGesture_Community_Edition\models\phanloai_cuchitay.h5"

# Tải mô hình
try:
    model = keras.models.load_model(model_path, compile=False)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Danh sách nhãn của mô hình
labels = ['fist','open_palm','thumbs_up']
# Hàm dự đoán cử chỉ từ ảnh đầu vào
def predict_gesture(image):
    if model is None:
        return "Unknown"
    
    try:
        # Chuyển ảnh sang định dạng RGB (nếu cần)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Resize ảnh về kích thước mà mô hình yêu cầu
        image = cv2.resize(image, (256, 256))
        
        # Chuẩn hóa ảnh (giá trị từ 0 đến 1)
        image = np.expand_dims(image, axis=0) / 255.0
        
        # Dự đoán cử chỉ từ mô hình
        prediction = model.predict(image, verbose=0)[0]
        
        # Trả về nhãn có xác suất cao nhất
        predicted_label = labels[np.argmax(prediction)]
        return predicted_label
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Unknown"
