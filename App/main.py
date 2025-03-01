import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Hand Gesture Control")
root.geometry("1200x800")

# Tạo frame cho video feed (bao gồm nhãn và canvas video)
frame_video = tk.Frame(root, bg="black")
frame_video.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")

# Thêm nhãn tên cho frame_video
label_video = tk.Label(frame_video, text="Video Feed", font=("Arial", 14), bg="black", fg="white")
label_video.pack(pady=5)

# Tạo canvas cho video feed
canvas_video = tk.Canvas(frame_video, bg="gray")
canvas_video.pack(fill="both", expand=True)

# Tạo frame cho control panel (bỏ viền đen)
frame_control_panel = tk.Frame(root, bg="lightgreen")
frame_control_panel.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Thêm nhãn tên cho frame_control_panel
label_control_panel = tk.Label(frame_control_panel, text="Control Panel", font=("Arial", 14), bg="lightgreen", fg="black")
label_control_panel.pack(pady=5)

# Tạo canvas cho control panel
canvas_control_panel = tk.Canvas(frame_control_panel, bg="lightgreen")
canvas_control_panel.pack(padx=10, pady=10, fill="both", expand=True)

# Hàm giả lập chức năng điều khiển
def volume_up():
    print("Volume Up")

def volume_down():
    print("Volume Down")

def brightness_up():
    print("Brightness Up")

def brightness_down():
    print("Brightness Down")

def zoom_in():
    print("Zoom In")

def zoom_out():
    print("Zoom Out")

# Thêm các nút điều khiển vào canvas_control_panel
button_volume_up = tk.Button(canvas_control_panel, text="Volume Up", command=volume_up)
button_volume_up.place(relx=0.5, rely=0.1, anchor="center")

button_volume_down = tk.Button(canvas_control_panel, text="Volume Down", command=volume_down)
button_volume_down.place(relx=0.5, rely=0.2, anchor="center")

button_brightness_up = tk.Button(canvas_control_panel, text="Brightness Up", command=brightness_up)
button_brightness_up.place(relx=0.5, rely=0.3, anchor="center")

button_brightness_down = tk.Button(canvas_control_panel, text="Brightness Down", command=brightness_down)
button_brightness_down.place(relx=0.5, rely=0.4, anchor="center")

button_zoom_in = tk.Button(canvas_control_panel, text="Zoom In", command=zoom_in)
button_zoom_in.place(relx=0.5, rely=0.5, anchor="center")

button_zoom_out = tk.Button(canvas_control_panel, text="Zoom Out", command=zoom_out)
button_zoom_out.place(relx=0.5, rely=0.6, anchor="center")

# Tạo frame cho feedback (vẽ mô phỏng MediaPipe)
frame_feedback = tk.Frame(root, bg="lightblue")
frame_feedback.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

# Thêm nhãn tên cho frame_feedback
label_feedback = tk.Label(frame_feedback, text="Hand Gesture Feedback", font=("Arial", 14), bg="lightblue", fg="black")
label_feedback.pack(pady=5)

# Thêm Canvas vào frame_feedback để vẽ mô phỏng (không có video feed)
canvas_feedback = tk.Canvas(frame_feedback, bg="lightblue")
canvas_feedback.pack(padx=10, pady=10, fill="both", expand=True)

# Cấu hình cửa sổ chính
root.grid_rowconfigure(0, weight=4)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=2)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)

# Mở video webcam
cap = cv2.VideoCapture(0)

def update_video():
    ret, frame = cap.read()
    if ret:
        # Chuyển đổi ảnh OpenCV (BGR) thành ảnh PIL (RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Lấy kích thước của canvas
        canvas_width = canvas_video.winfo_width()
        canvas_height = canvas_video.winfo_height()

        # Thay đổi kích thước ảnh sao cho vừa với canvas
        frame_resized = cv2.resize(frame, (canvas_width, canvas_height))

        # Chuyển ảnh đã thay đổi kích thước thành ảnh PIL
        img = Image.fromarray(frame_resized)
        img_tk = ImageTk.PhotoImage(img)
        
        # Cập nhật canvas_video
        canvas_video.create_image(0, 0, anchor="nw", image=img_tk)
        canvas_video.img_tk = img_tk  # Giữ tham chiếu để tránh ảnh bị xóa

    # Lặp lại sau mỗi 10ms
    root.after(10, update_video)

# Bắt đầu video feed
update_video()

# Bắt đầu giao diện người dùng
root.mainloop()

# Giải phóng webcam khi đóng cửa sổ
cap.release()
