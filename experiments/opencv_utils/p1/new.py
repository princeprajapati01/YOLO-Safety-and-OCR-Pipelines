import cv2
import random
import time

def get_bot_move():
	return random.choice(['Rock', 'Paper', 'Scissors'])

def get_result(user, bot):
	if user == bot:
		return "Draw"
	if (user == 'Rock' and bot == 'Scissors') or (user == 'Paper' and bot == 'Rock') or (user == 'Scissors' and bot == 'Paper'):
		return "You Win!"
	return "Bot Wins!"

def detect_hand_sign():
	# Placeholder: randomly return a move for demonstration
	# In a real implementation, this would use hand landmarks to determine the gesture
	return random.choice(['Rock', 'Paper', 'Scissors', None])

def main():
	cap = cv2.VideoCapture(0)
	
	if not cap.isOpened():
		print("Cannot open camera")
		return
	print("Show your hand: Fist=Rock, Open=Paper, V=Scissors. Press 'q' to quit.")
	print("Note: Hand detection is simplified - press SPACE to make a move.")
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
		
		# Add instruction text
		cv2.putText(frame, "Press SPACE to play, Q to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
		
		# Show last round result
		if user_move and bot_move and result:
			text = f'You: {user_move}  Bot: {bot_move}  Result: {result}'
			cv2.putText(frame, text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2, cv2.LINE_AA)
		
		cv2.imshow('Rock Paper Scissors (Hand)', frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break
		elif key == ord(' '):  # Space key to play
			if time.time() - last_move_time > cooldown:
				user_move = detect_hand_sign()
				if user_move:
					bot_move = get_bot_move()
					result = get_result(user_move, bot_move)
					last_move_time = time.time()
	
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
