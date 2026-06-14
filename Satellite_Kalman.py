import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture('Satellite Tracking.avi')

# Kalman Filter
kf = cv2.KalmanFilter(4, 2)

# State: [x, y, vx, vy]
kf.transitionMatrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
], np.float32)

kf.measurementMatrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
], np.float32)

kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * 0.5
kf.errorCovPost = np.eye(4, dtype=np.float32)

initialized = False
frame_num = 0

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    frame_num += 1

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold bright objects
    _, thresh = cv2.threshold(
        gray,
        200,
        255,
        cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:

        # Largest bright object
        largest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest)

        cx = x + w // 2
        cy = y + h // 2

        measurement = np.array([
            [np.float32(cx)],
            [np.float32(cy)]
        ])

        if not initialized:

            kf.statePost = np.array([
                [np.float32(cx)],
                [np.float32(cy)],
                [0],
                [0]
            ])

            initialized = True

        # Prediction step
        prediction = kf.predict()

        # Correction step
        estimated = kf.correct(measurement)

        est_x = estimated[0][0]
        est_y = estimated[1][0]

        vx = estimated[2][0]
        vy = estimated[3][0]

        speed = np.sqrt(vx**2 + vy**2)

        print(
            f"Frame {frame_num}: "
            f"Position=({est_x:.1f}, {est_y:.1f}) "
            f"Velocity=({vx:.2f}, {vy:.2f}) "
            f"Speed={speed:.2f} pixels/frame"
        )

        # Draw measured position
        cv2.circle(
            frame,
            (cx, cy),
            5,
            (0,255,0),
            -1
        )

        # Draw estimated position
        cv2.circle(
            frame,
            (int(est_x), int(est_y)),
            5,
            (0,0,255),
            -1
        )

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()