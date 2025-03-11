import module_gesture_recognition
import cv2

test_image = r"D:\Project\HandGesture_Community_Edition\models\data2\test\open_palm\scene00041.png"

image = cv2.imread(test_image)
if image is None:
    print("❌ Lỗi: Không tìm thấy ảnh test!")
else:
    gesture = module_gesture_recognition.predict_gesture(image)
    print(f"🖐 Nhận diện cử chỉ: {gesture}")
