import cv2
import module_hand_tracking
import module_mouse_control
import module_ui
import pyautogui
import numpy as np
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

# Biến trạng thái điều khiển
current_control = None  # Trạng thái mặc định, chưa chọn điều khiển

# Hàm xử lý các nút trên giao diện
def adjust_volume():
    global current_control
    current_control = "volume"
    print("Chế độ Volume được kích hoạt!")

def adjust_brightness():
    global current_control
    current_control = "brightness"
    print("Chế độ Brightness được kích hoạt!")

def adjust_zoom():
    global current_control
    current_control = "zoom"
    print("Chế độ Zoom được kích hoạt!")

# Gắn hàm vào các nút giao diện
ui.btn_volume.config(command=adjust_volume)
ui.btn_brightness.config(command=adjust_brightness)
ui.btn_zoom.config(command=adjust_zoom)

# Hàm cập nhật video và xử lý logic
def update_video():
    ret, frame = cap.read()
    if not ret:
        ui.root.after(10, update_video)
        return

    # Xử lý hiển thị video trên giao diện
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (ui.canvas_video.winfo_width(), ui.canvas_video.winfo_height()))
    ui.update_video_canvas(frame_resized)

    # Phát hiện bàn tay
    results = hand_tracker.detect_hands(frame)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Xử lý tùy theo chế độ được chọn
            if current_control == "volume":
                distance = calculate_distance(landmarks)
                volume_control.adjust_volume(distance)
                print(f"Điều chỉnh âm lượng với khoảng cách: {distance:0.9f}")

            elif current_control == "brightness":
                distance = calculate_distance(landmarks)
                brightness_control.adjust_brightness(distance)
                print(f"Điều chỉnh độ sáng với khoảng cách: {distance:0.9f}")

            elif current_control == "zoom":
                distance = calculate_distance(landmarks)
                zoom_control.adjust_zoom(distance)
                print(f"Điều chỉnh zoom với khoảng cách: {distance:0.9f}")

            # Hiển thị feedback bàn tay lên giao diện
            ui.update_feedback_canvas(landmarks)

    ui.root.after(10, update_video)  # Lặp lại sau 10ms

def calculate_distance(landmarks):
    """Tính khoảng cách giữa ngón cái và ngón trỏ."""
    index_tip = landmarks.landmark[module_hand_tracking.mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = landmarks.landmark[module_hand_tracking.mp_hands.HandLandmark.THUMB_TIP]

    # Khoảng cách giữa ngón cái và ngón trỏ để xác định mức thay đổi
    distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5
     # Cập nhật màu sắc nút khi nhận diện cử chỉ
    ui.update_button_color(gesture_name)
    
    if gesture_name == "thumbs_up":
        volume_control.adjust_volume(distance)
    elif gesture_name == "fist":
        brightness_control.adjust_brightness(distance)
    elif gesture_name == "open_palm":
        zoom_control.adjust_zoom(distance)

ui.run(update_video)
cap.release()
cv2.destroyAllWindows()
