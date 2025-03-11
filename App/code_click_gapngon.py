import tkinter as tk
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import os
import pyautogui
import time
import numpy as np

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Hand Gesture Control")
root.iconbitmap(r"D:\Project\HandGesture_Community_Edition\Assets\logo\hand_gesture_logo.ico")
root.geometry("1200x800")

# Tạo frame cho video feed
frame_video = tk.Frame(root, bg="black")
frame_video.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")

# Tạo canvas cho video feed
canvas_video = tk.Canvas(frame_video, bg="black")
canvas_video.pack(fill="both", expand=True)

# Thêm nhãn tên cho frame_video
label_video = tk.Label(frame_video, text="Video Feed", font=("Arial", 14), bg="black", fg="white")
label_video.place(relx=0.5, rely=0.05, anchor="n")

# Tạo frame cho panel điều khiển
frame_control_panel = tk.Frame(root, bg="lightgreen")
frame_control_panel.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

# Thêm nhãn tên cho frame_control_panel
label_control_panel = tk.Label(frame_control_panel, text="Control Panel", font=("Arial", 14), bg="lightgreen", fg="black")
label_control_panel.pack(pady=5)

# Tạo frame cho panel feedback (vẽ mô phỏng MediaPipe)
frame_feedback = tk.Frame(root, bg="lightblue")
frame_feedback.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Thêm nhãn tên cho frame_feedback
label_feedback = tk.Label(frame_feedback, text="Hand Gesture Feedback", font=("Arial", 14), bg="lightblue", fg="black")
label_feedback.pack(pady=5)

# Thêm Canvas vào frame_feedback để vẽ mô phỏng
canvas_feedback = tk.Canvas(frame_feedback, bg="lightblue")
canvas_feedback.pack(padx=10, pady=10, fill="both", expand=True)

# Mở webcam
cap = cv2.VideoCapture(0)

# Khởi tạo MediaPipe cho cử chỉ tay
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Lấy kích thước màn hình
screen_width, screen_height = pyautogui.size()

# Lưu vị trí con trỏ để làm mượt
pos_history = []

# Trạng thái click chuột
click_state = False
click_delay = 10  # Số frame tối thiểu giữa 2 lần click
frame_counter = 0  # Đếm số frame từ lần click trước

# Hàm cập nhật video feed và nhận diện cử chỉ tay
def update_video():
    global frame_counter, click_state

    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (canvas_video.winfo_width(), canvas_video.winfo_height()))

        img = Image.fromarray(frame_resized)
        img_tk = ImageTk.PhotoImage(image=img)
        canvas_video.create_image(0, 0, anchor="nw", image=img_tk)
        canvas_video.img_tk = img_tk

        # Nhận diện cử chỉ tay
        results = hands.process(frame_rgb)
        canvas_feedback.delete("all")

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_pip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

                # Tính khoảng cách giữa đầu ngón trỏ và khớp gần nhất
                distance = ((index_tip.x - index_pip.x) ** 2 + (index_tip.y - index_pip.y) ** 2) ** 0.5

                # Tính tọa độ chuột
                mouse_x = int(index_tip.x * screen_width)
                mouse_y = int(index_tip.y * screen_height)

                # Làm mượt vị trí chuột bằng trung bình cộng
                pos_history.append((mouse_x, mouse_y))
                if len(pos_history) > 5:
                    pos_history.pop(0)

                smooth_x = int(np.mean([p[0] for p in pos_history]))
                smooth_y = int(np.mean([p[1] for p in pos_history]))

                # Giới hạn tần suất cập nhật để tránh rung lắc
                if len(pos_history) > 1:
                    prev_x, prev_y = pos_history[-2]
                    movement_threshold = 10
                    if abs(smooth_x - prev_x) > movement_threshold or abs(smooth_y - prev_y) > movement_threshold:
                        pyautogui.moveTo(smooth_x, smooth_y)

                # Kiểm tra trạng thái gập ngón trỏ để click
                if distance < 0.05 and not click_state and frame_counter >= click_delay:
                    pyautogui.click()
                    click_state = True  # Đánh dấu đã click
                    frame_counter = 0

                elif distance >= 0.05:
                    click_state = False  # Reset trạng thái click khi mở ngón trỏ

                frame_counter += 1  # Tăng bộ đếm frame

                # Vẽ landmark trên feedback
                for lm in landmarks.landmark:
                    lx, ly = int(lm.x * canvas_feedback.winfo_width()), int(lm.y * canvas_feedback.winfo_height())
                    canvas_feedback.create_oval(lx-4, ly-4, lx+4, ly+4, fill="red")

                # Tô đậm đầu ngón trỏ
                canvas_feedback.create_oval(int(index_tip.x * canvas_feedback.winfo_width()) - 6,
                                            int(index_tip.y * canvas_feedback.winfo_height()) - 6,
                                            int(index_tip.x * canvas_feedback.winfo_width()) + 6,
                                            int(index_tip.y * canvas_feedback.winfo_height()) + 6,
                                            fill="yellow")

                # Vẽ kết nối giữa các điểm
                for connection in mp_hands.HAND_CONNECTIONS:
                    start_idx, end_idx = connection
                    sx, sy = int(landmarks.landmark[start_idx].x * canvas_feedback.winfo_width()), int(landmarks.landmark[start_idx].y * canvas_feedback.winfo_height())
                    ex, ey = int(landmarks.landmark[end_idx].x * canvas_feedback.winfo_width()), int(landmarks.landmark[end_idx].y * canvas_feedback.winfo_height())
                    canvas_feedback.create_line(sx, sy, ex, ey, fill="white", width=2)

    root.after(10, update_video)

update_video()

# Cấu hình cửa sổ chính
root.grid_rowconfigure(0, weight=4)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=2)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
cap.release()
