#module_ui.py
import tkinter as tk
from PIL import Image, ImageTk
import mediapipe as mp

class HandTrackingUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hand Gesture Control")
        #self.root.geometry("860x550")
        self.root.geometry("1200x800")
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Đặt icon cho ứng dụng
        icon_path = r"D:\Project\HandGesture_Community_Edition\Assets\logo\hand_gesture_logo.ico"
        self.root.iconbitmap(icon_path)

        # Frame chứa video
        self.frame_video = tk.Frame(self.root, bg="black", bd=2, relief="sunken")
        self.frame_video.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")

        self.label_video = tk.Label(self.frame_video, text="Video Feed", font=("Arial", 14, "bold"), bg="black", fg="white")
        self.label_video.pack(anchor="n", pady=5)

        self.canvas_video = tk.Canvas(self.frame_video, bg="black")
        self.canvas_video.pack(fill="both", expand=True)

        # Frame hướng dẫn user
        self.frame_guiding = tk.Frame(self.root, bg="orange", bd=2, relief="sunken")
        self.frame_guiding.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.label_guiding = tk.Label(self.frame_guiding, text="User Guiding", font=("Arial", 14, "bold"), bg="orange", fg="black")
        self.label_guiding.pack(anchor="n", pady=5)

        self.label_gesture_info = tk.Label(self.frame_guiding, text="Đang chờ nhận diện...", font=("Arial", 12), bg="orange", fg="black")
        self.label_gesture_info.pack(pady=5)

        # Frame điều khiển
        self.frame_control_panel = tk.Frame(self.root, bg="lightgreen", bd=2, relief="sunken")
        self.frame_control_panel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_control_panel = tk.Label(self.frame_control_panel, text="Control Panel", font=("Arial", 14, "bold"), bg="lightgreen", fg="black")
        self.label_control_panel.pack(anchor="n", pady=5)

        self.btn_volume = tk.Button(self.frame_control_panel, text="Volume", font=("Arial", 12), bg="white", fg="black", command=self.adjust_volume)
        self.btn_volume.pack(pady=5, padx=10, fill="x")

        self.btn_brightness = tk.Button(self.frame_control_panel, text="Brightness", font=("Arial", 12), bg="white", fg="black", command=self.adjust_brightness)
        self.btn_brightness.pack(pady=5, padx=10, fill="x")

        self.btn_zoom = tk.Button(self.frame_control_panel, text="Zoom", font=("Arial", 12), bg="white", fg="black", command=self.adjust_zoom)
        self.btn_zoom.pack(pady=5, padx=10, fill="x")

        # Thêm hiệu ứng hover
        for btn in [self.btn_volume, self.btn_brightness, self.btn_zoom]:
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="gray", fg="white"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="white", fg="black"))
            btn.bind("<ButtonPress>", lambda e, b=btn: b.config(bg="darkgray"))
            btn.bind("<ButtonRelease>", lambda e, b=btn: b.config(bg="gray"))

        # Frame chứa feedback
        self.frame_feedback = tk.Frame(self.root, bg="lightblue", bd=2, relief="sunken")
        self.frame_feedback.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.label_feedback = tk.Label(self.frame_feedback, text="Hand Gesture Feedback", font=("Arial", 14, "bold"), bg="lightblue", fg="black")
        self.label_feedback.pack(anchor="n", pady=5)

        self.canvas_feedback = tk.Canvas(self.frame_feedback, bg="lightblue")
        self.canvas_feedback.pack(padx=10, pady=10, fill="both", expand=True)
        
    def adjust_volume(self):
        print("Adjusting Volume")

    def adjust_brightness(self):
        print("Adjusting Brightness")

    def adjust_zoom(self):
        print("Adjusting Zoom")

    def update_video_canvas(self, frame):
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)
        self.canvas_video.create_image(0, 0, anchor="nw", image=img_tk)
        self.canvas_video.img_tk = img_tk  # Tránh bị mất ảnh

    def update_feedback_canvas(self, hand_landmarks):
        self.canvas_feedback.delete("all")
    
        width, height = self.canvas_feedback.winfo_width(), self.canvas_feedback.winfo_height()
    
        for lm in hand_landmarks.landmark:
            lx, ly = int(lm.x * width), int(lm.y * height)
            self.canvas_feedback.create_oval(lx-4, ly-4, lx+4, ly+4, fill="red")

        index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        self.canvas_feedback.create_oval(int(index_tip.x * width) - 6,
                                         int(index_tip.y * height) - 6,
                                         int(index_tip.x * width) + 6,
                                         int(index_tip.y * height) + 6,
                                         fill="yellow")

        for connection in mp.solutions.hands.HAND_CONNECTIONS:
            start_idx, end_idx = connection
            start = hand_landmarks.landmark[start_idx]
            end = hand_landmarks.landmark[end_idx]

            sx, sy = int(start.x * width), int(start.y * height)
            ex, ey = int(end.x * width), int(end.y * height)

            self.canvas_feedback.create_line(sx, sy, ex, ey, fill="white", width=2)

    def update_gesture_info(self, gesture_name):
        self.label_gesture_info.config(text=f"Hệ thống nhận diện: {gesture_name}", font=("Arial", 12, "bold"))

    def update_button_color(self, gesture_name):
        """Cập nhật màu sắc của các nút điều khiển khi nhận diện cử chỉ"""
        # Đặt lại màu nền các nút về mặc định
        self.btn_volume.config(bg="white")
        self.btn_brightness.config(bg="white")
        self.btn_zoom.config(bg="white")

        if gesture_name == "thumbs_up":
            self.btn_volume.config(bg="red")  # Đổi màu nút Volume thành đỏ
        elif gesture_name == "fist":
            self.btn_brightness.config(bg="red")  # Đổi màu nút Brightness thành đỏ
        elif gesture_name == "open_palm":
            self.btn_zoom.config(bg="red")  # Đổi màu nút Zoom thành đỏ
    
    def run(self, update_func):
        self.root.after(10, update_func)
        self.root.mainloop()