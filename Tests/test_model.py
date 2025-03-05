import tensorflow as tf
import numpy as np
import cv2
import os

# Đường dẫn đến mô hình đã huấn luyện
MODEL_PATH = r"D:\Project\HandGesture_Community_Edition\models\my_model.keras"

# Load mô hình đã huấn luyện
model = tf.keras.models.load_model(MODEL_PATH)

# Thông tin về mô hình
model.summary()

# Danh sách nhãn của các lớp (cập nhật theo mô hình của bạn)
CLASS_NAMES = ["fist", "thumb_up", "open_hand"]  # Thay thế bằng nhãn thực tế

# Đọc và xử lý ảnh đầu vào
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))  # Thay đổi kích thước theo mô hình
    img = img / 255.0  # Chuẩn hóa ảnh
    img = np.expand_dims(img, axis=0)  # Thêm batch dimension
    return img

# Dự đoán trên ảnh bất kỳ
def predict_image(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    class_index = np.argmax(predictions)
    confidence = np.max(predictions)
    print(f"Dự đoán: {CLASS_NAMES[class_index]} (Độ tin cậy: {confidence:.2f})")
    return CLASS_NAMES[class_index], confidence

# Test với ảnh mẫu
if __name__ == "__main__":
    test_image_path = r"D:\Project\HandGesture_Community_Edition\models\data2\test\thumbs_up\scene00041.png"  # Đổi đường dẫn tới ảnh test của bạn
    if os.path.exists(test_image_path):
        predict_image(test_image_path)
    else:
        print("Ảnh test không tồn tại, hãy kiểm tra lại đường dẫn!")