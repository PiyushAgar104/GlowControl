import cv2, mediapipe as mp, math
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

while True:
    ok, frame = cap.read()
    if not ok: break

    frame = cv2.flip(frame, 1)
    r = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if r.multi_hand_landmarks:
        h, w, _ = frame.shape
        hand = r.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

        x1,y1 = int(hand.landmark[4].x*w), int(hand.landmark[4].y*h)
        x2,y2 = int(hand.landmark[8].x*w), int(hand.landmark[8].y*h)

        d = math.hypot(x2-x1, y2-y1)
        b = int(max(0, min(100, (d-30)*100/220)))
        sbc.set_brightness(b)

        cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.putText(frame,f"Brightness: {b}%",(20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,.8,(0,255,0),2)

    cv2.imshow("GestureGlow", frame)
    if cv2.waitKey(1) & 255 == ord("q"): break

cap.release()
cv2.destroyAllWindows()