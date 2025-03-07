import pyautogui

class VolumeControl:
    def __init__(self):
        self.prev_distance = None

    def adjust_volume(self, distance):
        if self.prev_distance is None:
            self.prev_distance = distance
            return

        threshold = 0.02  # Chỉ thay đổi khi khoảng cách tăng/giảm lớn hơn mức này

        if distance > self.prev_distance + threshold:
            pyautogui.press("volumeup")
            print("🔊 Tăng âm lượng")
        elif distance < self.prev_distance - threshold:
            pyautogui.press("volumedown")
            print("🔉 Giảm âm lượng")

        self.prev_distance = distance
