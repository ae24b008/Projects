import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture('Satellite Tracking.avi')

# Parameters
num_frames = 5  # Number of frames to sample
frame_interval = 10  # Interval between sampled frames
frame_count = 0
positions_per_frame = []

while cap.isOpened() and len(positions_per_frame) < num_frames:
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % frame_interval == 0:
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Threshold to detect white spots
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Store positions of detected white spots in this frame
        current_positions = set()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            center = (x + w // 2, y + h // 2)
            current_positions.add(center)
        
        positions_per_frame.append(current_positions)
    
    frame_count += 1  # Increment frame count

cap.release()

# Find common stationary spot
if positions_per_frame:
    common_positions = set.intersection(*positions_per_frame)
    print("Stationary Spot Position:", common_positions if common_positions else "None found")
else:
    print("No frames processed.")