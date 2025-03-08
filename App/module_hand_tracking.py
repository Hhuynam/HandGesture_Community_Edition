# module_hand_tracking.py
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

class HandTracker:
    def __init__(self, min_detection_confidence=0.7, min_tracking_confidence=0.7):
        self.hands = mp_hands.Hands(min_detection_confidence=min_detection_confidence,
                                    min_tracking_confidence=min_tracking_confidence)
    
    def detect_hands(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(frame_rgb)
    
    def is_five_fingers_up(self, hand_landmarks):
        tips = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
                mp_hands.HandLandmark.PINKY_TIP]
        
        pips = [mp_hands.HandLandmark.THUMB_IP, mp_hands.HandLandmark.INDEX_FINGER_PIP,
                mp_hands.HandLandmark.MIDDLE_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_PIP,
                mp_hands.HandLandmark.PINKY_PIP]
        
        count = sum(1 for tip, pip in zip(tips, pips) if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)
        return count == 5 
