#module_zoom.py
import pyautogui

class ZoomControl:
    def __init__(self):
        self.prev_distance = None

    def adjust_zoom(self, distance):
        if self.prev_distance is None:
            self.prev_distance = distance
            return

        if distance > self.prev_distance + 5:
            pyautogui.hotkey("ctrl", "+")
            print("Zoom In")
        elif distance < self.prev_distance - 5:
            pyautogui.hotkey("ctrl", "-")
            print("Zoom Out")

        self.prev_distance = distance
