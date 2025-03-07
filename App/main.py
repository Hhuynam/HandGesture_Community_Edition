import cv2
import module_hand_tracking
import module_mouse_control
import module_ui
import pyautogui
import numpy as np
from module_model import new_model
from module_gesture_recognition import predict_gesture, labels  # Nhận diện cử chỉ
from module_brightness import BrightnessControl  # Điều chỉnh độ sáng
from module_volume import VolumeControl  # Điều chỉnh âm lượng
from module_zoom import ZoomControl  # Điều chỉnh zoom

# Khởi tạo webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Khởi tạo các module
hand_tracker = module_hand_tracking.HandTracker()
mouse_controller = module_mouse_control.MouseController(screen_width, screen_height)
ui = module_ui.HandTrackingUI()
brightness_control = BrightnessControl()
volume_control = VolumeControl()
zoom_control = ZoomControl()

def update_video():
    ret, frame = cap.read()
    if not ret:
        ui.root.after(10, update_video)
        return
    
    results = hand_tracker.detect_hands(frame)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if ui.canvas_video.winfo_width() > 0 and ui.canvas_video.winfo_height() > 0:
        frame_resized = cv2.resize(frame_rgb, (ui.canvas_video.winfo_width(), ui.canvas_video.winfo_height()))
        ui.update_video_canvas(frame_resized)
    
    ui.canvas_feedback.delete("all")

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            index_tip = landmarks.landmark[module_hand_tracking.mp_hands.HandLandmark.INDEX_FINGER_TIP]
            mouse_controller.move_mouse(index_tip)
            mouse_controller.click_mouse(hand_tracker.is_five_fingers_up(landmarks))
            ui.update_feedback_canvas(landmarks)

            # Nhận diện cử chỉ
            gesture_name = recognize_gesture(frame, landmarks)

            # Xử lý điều khiển dựa trên cử chỉ nhận diện được
            process_gesture_control(gesture_name, landmarks)

    ui.root.update_idletasks()
    ui.root.after(10, update_video)

def recognize_gesture(frame, landmarks):
    """Dự đoán cử chỉ từ model"""
    x_min = int(min([lm.x for lm in landmarks.landmark]) * frame.shape[1])
    x_max = int(max([lm.x for lm in landmarks.landmark]) * frame.shape[1])
    y_min = int(min([lm.y for lm in landmarks.landmark]) * frame.shape[0])
    y_max = int(max([lm.y for lm in landmarks.landmark]) * frame.shape[0])

    hand_img = frame[y_min:y_max, x_min:x_max]
    gesture_name = predict_gesture(hand_img)

    print(f"Nhận diện: {gesture_name}")

    # Cập nhật thông báo trên UI
    ui.update_gesture_info(gesture_name)
    return gesture_name

def process_gesture_control(gesture_name, landmarks):
    """Xử lý điều khiển dựa trên cử chỉ nhận diện"""
    index_tip = landmarks.landmark[module_hand_tracking.mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = landmarks.landmark[module_hand_tracking.mp_hands.HandLandmark.THUMB_TIP]

    # Khoảng cách giữa ngón cái và ngón trỏ để xác định mức thay đổi
    distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5

    if gesture_name == "thumb":
        volume_control.adjust_volume(distance)
    elif gesture_name == "fist":
        brightness_control.adjust_brightness(distance)
    elif gesture_name == "open_hand":
        zoom_control.adjust_zoom(distance)

# Hiển thị kiến trúc model trước khi chạy chương trình
new_model.summary()
ui.run(update_video)
cap.release()
cv2.destroyAllWindows()
