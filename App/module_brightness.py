import screen_brightness_control as sbc

class BrightnessControl:
    def __init__(self):
        self.prev_distance = None

    def adjust_brightness(self, distance):
        current_brightness = sbc.get_brightness(display=0)[0]

        if self.prev_distance is None:
            self.prev_distance = distance
            return

        threshold = 0.02  # Giảm mức nhạy cảm

        if distance > self.prev_distance + threshold:
            sbc.set_brightness(min(current_brightness + 5, 100))
            print("Tăng độ sáng")
        elif distance < self.prev_distance - threshold:
            sbc.set_brightness(max(current_brightness - 5, 0))
            print("Giảm độ sáng")

        self.prev_distance = distance
