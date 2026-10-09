import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,        # False treats input as a continuous video stream
    max_num_hands=2,                # Maximum number of hands to track
    min_detection_confidence=0.5,   # Threshold for initial hand detection
    min_tracking_confidence=0.5,     # Threshold for tracking landmarks
    model_complexity=1
)

def process_with_mp(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    media_pipe_result = hands.process(frame_rgb)

    return media_pipe_result

def draw(media_pipe_result,frame):
        if media_pipe_result.multi_hand_landmarks:
            for hand_landmarks in media_pipe_result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

def close():
     hands.close()