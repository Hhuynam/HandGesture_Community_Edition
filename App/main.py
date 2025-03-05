# main.py
import cv2
import module_hand_tracking
import module_mouse_control
import module_ui
import pyautogui

cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

hand_tracker = module_hand_tracking.HandTracker()
mouse_controller = module_mouse_control.MouseController(screen_width, screen_height)
ui = module_ui.HandTrackingUI()

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
    
    ui.root.update_idletasks()
    ui.root.after(10, update_video)

ui.run(update_video)
cap.release()
cv2.destroyAllWindows()