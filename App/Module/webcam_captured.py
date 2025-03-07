import cv2
import os

# Định nghĩa đường dẫn dataset
dataset_path = r"D:\Project\HandGesture_Community_Edition\models\data"
mode_labels = ["fist", "open_palm", "thumbs_up"]

# Tạo thư mục nếu chưa có
for label in mode_labels:
    os.makedirs(os.path.join(dataset_path, label), exist_ok=True)

# Kết nối với webcam (0 là chỉ số camera mặc định)
cap = cv2.VideoCapture(0)

# Kiểm tra camera có hoạt động không
if not cap.isOpened():
    print("Không thể kết nối với webcam! Kiểm tra lại kết nối camera.")
    exit()

current_mode = 0  # Mặc định Mode_1
count = 0  # Đếm số ảnh đã chụp

print("Nhấn phím 1-3 để chọn mode (fist, open_palm, thumbs_up), SPACE để chụp, ESC để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không nhận được frame từ webcam!")
        break
    
    # Hiển thị chế độ hiện tại
    cv2.putText(frame, f"Mode: {mode_labels[current_mode]}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Webcam Capture", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key in [ord(str(i)) for i in range(1, 4)]:  # Chọn mode
        current_mode = int(chr(key)) - 1
        print(f"Đã chọn {mode_labels[current_mode]}")
    
    elif key == ord(' '):  # Chụp ảnh
        img_path = os.path.join(dataset_path, mode_labels[current_mode], f"webcam_img_{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"Đã lưu: {img_path}")
    
    elif key == 27:  # Thoát
        break

cap.release()
cv2.destroyAllWindows()
