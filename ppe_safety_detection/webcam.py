from ultralytics import YOLO
import cv2


model = YOLO("best.pt")  


cap = cv2.VideoCapture(0)  

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_path = "output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO Prediction
    results = model(frame)

    # Draw Results
    annotated_frame = results[0].plot()

    # Show Live Result
    cv2.imshow("YOLO Detection", annotated_frame)

    # Save Output Video
    out.write(annotated_frame)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing Complete")
print("Saved Output Video:", output_path)