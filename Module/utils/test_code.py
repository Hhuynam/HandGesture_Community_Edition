import tensorflow as tf
import numpy as np
import cv2
import os

# Đường dẫn đến mô hình đã huấn luyện
model_path = r"D:\Project\HandGesture_Community_Edition\Train\model_handgesture.h5"
model = tf.keras.models.load_model(model_path)

# Danh sách các lớp cử chỉ tay
gesture_classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

# Hàm dự đoán ảnh đầu vào
def predict_gesture(image_path):
    img_size = (50, 50)  # Kích thước ảnh dùng để huấn luyện
    image = cv2.imread(image_path)
    image = cv2.resize(image, img_size)  # Resize ảnh
    image = image / 255.0  # Chuẩn hóa ảnh
    image = np.expand_dims(image, axis=0)  # Thêm batch dimension

    # Dự đoán bằng mô hình
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)  # Lấy lớp có xác suất cao nhất
    confidence = np.max(predictions)  # Xác suất dự đoán

    return gesture_classes[predicted_class], confidence

# Test dự đoán với một ảnh bất kỳ
test_image = r"D:\Project\HandGesture_Community_Edition\Dataset\test\18\917.jpg"  # Thay ảnh test vào đây
predicted_gesture, confidence = predict_gesture(test_image)
print(f"Cử chỉ dự đoán: {predicted_gesture}, Độ tin cậy: {confidence:.2f}")
