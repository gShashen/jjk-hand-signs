import cv2
import time
import hand_tracker as ht


def calculate_fps(prev_time):
    """Return the current FPS and the new timestamp for the next call."""
    current_time = time.perf_counter()
    fps = 1 / max(current_time - prev_time, 1e-6)
    return fps, current_time


def draw_fps(frame, fps):
    """Draw the FPS value onto the top-left corner of the frame."""
    cv2.putText(frame, f"FPS: {fps:.0f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Could not open the camera")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # or cap.set(3, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # or cap.set(4, 720)

print("Press ESC to exit the window")

prev_time = time.perf_counter()

try:
    while True:
        frame_is_successful, frame = cam.read()

        if not frame_is_successful:
            print("Can not get the frame")
            break

        frame = cv2.flip(frame,1)

        media_pipe_result = ht.process_with_mp(frame)
        ht.draw(media_pipe_result,frame)

        fps, prev_time = calculate_fps(prev_time)
        draw_fps(frame, fps)

        cv2.imshow("JJK Hand signs", frame)

        if cv2.waitKey(1) & 0XFF == 27:
            break
finally:
    ht.close()
    cam.release()
    cv2.destroyAllWindows()