# code_chup_anh_dataset_droidcam.py: Dùng để tự chụp ảnh từ DroidCam cho dataset
import cv2
import os

# Định nghĩa đường dẫn dataset
dataset_path = "D:/Project/HandGesture_Community_Edition/Manual_Collection_Dataset"
mode_labels = ["Mode_1", "Mode_2", "Mode_3"]

# Tạo thư mục nếu chưa có
for label in mode_labels:
    os.makedirs(os.path.join(dataset_path, label), exist_ok=True)

# URL của DroidCam (cổng mặc định 4747)
droidcam_url = "http://192.168.0.103:4747/video"
cap = cv2.VideoCapture(droidcam_url)

# Kiểm tra camera có hoạt động không
if not cap.isOpened():
    print("Không thể kết nối DroidCam! Kiểm tra lại IP và cổng.")
    exit()

current_mode = 0  # Mặc định Mode_1
count = 0  # Đếm số ảnh đã chụp

print("Nhấn phím 1-3 để chọn mode, SPACE để chụp, ESC để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không nhận được frame từ DroidCam!")
        break
    
    # Hiển thị chế độ hiện tại
    cv2.putText(frame, f"Mode: {current_mode+1}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("DroidCam Capture", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key in [ord(str(i)) for i in range(1, 4)]:  # Chọn mode
        current_mode = int(chr(key)) - 1
        print(f"Đã chọn {mode_labels[current_mode]}")
    
    elif key == ord(' '):  # Chụp ảnh
        img_path = os.path.join(dataset_path, mode_labels[current_mode], f"droicam_img_{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"Đã lưu: {img_path}")
    
    elif key == 27:  # Thoát
        break

cap.release()
cv2.destroyAllWindows()
