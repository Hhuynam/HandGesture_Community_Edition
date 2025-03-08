# module_mouse_control.py
import pyautogui
import numpy as np

class MouseController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pos_history = []
        self.click_state = False
    
    def move_mouse(self, index_tip):
        mouse_x = int(index_tip.x * self.screen_width)
        mouse_y = int(index_tip.y * self.screen_height)
        
        self.pos_history.append((mouse_x, mouse_y))
        if len(self.pos_history) > 5:
            self.pos_history.pop(0)
        
        smooth_x = int(np.mean([p[0] for p in self.pos_history]))
        smooth_y = int(np.mean([p[1] for p in self.pos_history]))
        
        pyautogui.moveTo(smooth_x, smooth_y)
    
    def click_mouse(self, is_five_fingers_up):
        if is_five_fingers_up and not self.click_state:
            pyautogui.click()
            self.click_state = True
        elif not is_five_fingers_up:
            self.click_state = False
