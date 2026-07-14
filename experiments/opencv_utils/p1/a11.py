import cv2
import mediapipe as mp
import random
import time

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Hand detector
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Game variables
user_move = ""
bot_move = ""
result = ""

last_time = 0
cooldown = 2

def get_bot_move():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_result(user, bot):

    if user == bot:
        return "Draw"

    if (
        (user == "Rock" and bot == "Scissors") or
        (user == "Paper" and bot == "Rock") or
        (user == "Scissors" and bot == "Paper")
    ):
        return "You Win"

    return "Bot Wins"

def detect_gesture(hand_landmarks):

    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip, pip in zip(tip_ids, pip_ids):

        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    # Rock
    if total == 0:
        return "Rock"

    # Paper
    elif total == 5:
        return "Paper"

    # Scissors
    elif fingers[1] == 1 and fingers[2] == 1 and total == 2:
        return "Scissors"

    return None

while True:

    success, frame = cap.read()

    if not success:
        print("Camera error")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result_hands = hands.process(rgb)

    current_move = None

    if result_hands.multi_hand_landmarks:

        for hand_landmarks in result_hands.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            current_move = detect_gesture(hand_landmarks)

    # Game trigger
    if current_move and time.time() - last_time > cooldown:

        user_move = current_move

        bot_move = get_bot_move()

        result = get_result(user_move, bot_move)

        print("You:", user_move)
        print("Bot:", bot_move)
        print("Result:", result)
        print("----------------")

        last_time = time.time()

    # Display text
    cv2.putText(
        frame,
        f"You: {user_move}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Bot: {bot_move}",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        result,
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("Rock Paper Scissors AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()