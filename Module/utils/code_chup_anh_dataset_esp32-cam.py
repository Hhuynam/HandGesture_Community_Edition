# code_chup_anh_dataset_esp32-cam.py: Dùng để tự chụp ảnh từ ESP32-CAM cho dataset
import cv2
import os

# Định nghĩa đường dẫn dataset
dataset_path = "D:/Project/HandGesture_Community_Edition/Manual_Collection_Dataset"
mode_labels = ["Mode_1", "Mode_2", "Mode_3"]

# Tạo thư mục nếu chưa có
for label in mode_labels:
    os.makedirs(os.path.join(dataset_path, label), exist_ok=True)

# URL cố định của ESP32-CAM
esp_url = "http://192.168.0.108:81/stream"
cap = cv2.VideoCapture(esp_url)  # Đọc luồng video từ ESP32-CAM

# Kiểm tra camera có hoạt động không
if not cap.isOpened():
    print("Không thể mở ESP32-CAM! Kiểm tra URL và kết nối.")
    exit()

current_mode = 0  # Mặc định Mode_1
count = 0  # Đếm số ảnh đã chụp

print("Nhấn phím 1-3 để chọn mode, SPACE để chụp, ESC để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không nhận được frame từ ESP32-CAM!")
        break
    
    # Hiển thị chế độ hiện tại
    cv2.putText(frame, f"Mode: {current_mode+1}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("ESP32-CAM Capture", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key in [ord(str(i)) for i in range(1, 4)]:  # Chọn mode
        current_mode = int(chr(key)) - 1
        print(f"Đã chọn {mode_labels[current_mode]}")
    
    elif key == ord(' '):  # Chụp ảnh
        img_path = os.path.join(dataset_path, mode_labels[current_mode], f"img_{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"Đã lưu: {img_path}")
    
    elif key == 27:  # Thoát
        break

cap.release()
cv2.destroyAllWindows()