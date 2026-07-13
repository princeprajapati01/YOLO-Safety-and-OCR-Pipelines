import cv2
import random
import mediapipe.python.solutions.hands as hands_module
import mediapipe.python.solutions.drawing_utils as drawing_utils
import time

def get_bot_move():
	return random.choice(['Rock', 'Paper', 'Scissors'])

def get_result(user, bot):
	if user == bot:
		return "Draw"
	if (user == 'Rock' and bot == 'Scissors') or (user == 'Paper' and bot == 'Rock') or (user == 'Scissors' and bot == 'Paper'):
		return "You Win!"
	return "Bot Wins!"

def detect_hand_sign(hand_landmarks):
	# Simple logic: count extended fingers
	# Thumb: tip (4) > joint (3) in x for right hand, < for left hand
	# Fingers: tip (8, 12, 16, 20) > pip (6, 10, 14, 18) in y (for open)
	tips = [4, 8, 12, 16, 20]
	fingers = []
	# Thumb
	if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
		fingers.append(1)
	else:
		fingers.append(0)
	# Other 4 fingers
	for tip, pip in zip([8,12,16,20],[6,10,14,18]):
		if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
			fingers.append(1)
		else:
			fingers.append(0)
	total_fingers = sum(fingers)
	if total_fingers == 0:
		return 'Rock'
	elif total_fingers == 2:
		return 'Scissors'
	elif total_fingers == 5:
		return 'Paper'
	else:
		return None

def main():
	# Try camera indices 0, 1, 2
	cap = None
	for idx in range(3):
		cap = cv2.VideoCapture(idx)
		if cap.isOpened():
			print(f"Camera opened at index {idx}")
			break
		else:
			cap.release()
			cap = None
	if cap is None or not cap.isOpened():
		print("Cannot open any camera (tried indices 0, 1, 2). Make sure your webcam is connected and not used by another app.")
		return
	hands = hands_module.Hands(max_num_hands=1, min_detection_confidence=0.7)
	print("Show your hand: Fist=Rock, Open=Paper, V=Scissors. Press 'q' to quit.")
	user_move = None
	bot_move = None
	result = None
	last_move_time = 0
	cooldown = 2  # seconds between moves
	while True:
		ret, frame = cap.read()
		if not ret:
			print("Can't receive frame. Exiting...")
			break
		frame = cv2.flip(frame, 1)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		res = hands.process(rgb)
		move = None
		if res.multi_hand_landmarks:
			for hand_landmarks in res.multi_hand_landmarks:
				move = detect_hand_sign(hand_landmarks)
				drawing_utils.draw_landmarks(frame, hand_landmarks, hands_module.HAND_CONNECTIONS)
		# Show last round result
		if user_move and bot_move and result:
			text = f'You: {user_move}  Bot: {bot_move}  Result: {result}'
			cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2, cv2.LINE_AA)
		if move and (time.time() - last_move_time > cooldown):
			user_move = move
			bot_move = get_bot_move()
			result = get_result(user_move, bot_move)
			last_move_time = time.time()
		cv2.imshow('Rock Paper Scissors (Hand)', frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
