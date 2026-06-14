# Projects
# Satellite Detection and Line Extraction 

## Overview

This project implements an image-processing pipeline for detecting bright objects and extracting linear features from grayscale satellite imagery. The objective is to identify non-background pixels, detect potential satellite streaks or trails, and determine their geometric properties for further analysis.

## Methodology

The input image is first converted to grayscale and all non-black pixels are identified. These pixels are highlighted in red to visualize regions of interest. Edge detection is then performed using the Canny algorithm, followed by the Probabilistic Hough Transform to detect linear features within the image.

For each detected line, the program:

* Determines the start and end coordinates.
* Calculates the midpoint of the line segment.
* Displays the detected line in green on the processed image.
* Prints the midpoint coordinates for further analysis.

## Features

* Detection of all non-background pixels.
* Edge extraction using the Canny edge detector.
* Automatic line detection using the Hough Transform.
* Midpoint calculation for detected line segments.
* Visualization and saving of processed results.

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib

## Applications

This project can be applied to:

* Satellite and space-object detection.
* Analysis of streaks in astronomical images.
* Object trajectory estimation.
* Feature extraction in remote sensing imagery.

## Output

The program generates a processed image showing:

* Red pixels representing detected non-background regions.
* Green lines representing detected linear features.
* Printed midpoint coordinates for each detected line segment.

# Satellite Tracking and Velocity Estimation using Kalman Filter

## Overview

This project implements a computer vision-based satellite tracking system using Python and OpenCV. The program processes a video containing bright moving objects, detects the satellite in each frame, and applies a Kalman Filter to estimate its position and velocity. The filter reduces measurement noise and provides smooth trajectory tracking across consecutive frames.

## Objectives

* Detect bright satellite-like objects from video frames.
* Track the satellite's position over time.
* Estimate velocity components and overall speed.
* Visualize the tracking results on the video.
* Generate frame-by-frame tracking data for further analysis.

## Methodology

### 1. Frame Processing

The input video is read frame by frame using OpenCV. Each frame is converted to grayscale and thresholded to isolate bright objects from the background.

### 2. Object Detection

Contours are extracted from the thresholded image, and the largest bright object is identified as the target satellite. The centroid of the detected object is used as the measurement input.

### 3. Kalman Filter Tracking

A Kalman Filter with a constant-velocity motion model is implemented. The state vector consists of:

* Horizontal position (x)
* Vertical position (y)
* Horizontal velocity (vx)
* Vertical velocity (vy)

For each frame, the filter:

1. Predicts the next satellite position.
2. Updates the prediction using the measured position.
3. Estimates the satellite velocity and speed.

### 4. Visualization

The measured position and Kalman-filter-estimated position are drawn on the video frames, enabling visual verification of tracking performance.

## Results

The system provides:

* Satellite position in each frame.
* Velocity components (vx, vy).
* Speed magnitude.
* Smoothed trajectory estimates.
* Annotated tracking video output.

## Applications

* Satellite and space-object tracking.
* Astronomical image analysis.
* Motion estimation in aerospace systems.
* Object tracking under noisy measurement conditions.

## Technologies Used

* Python
* OpenCV
* NumPy
* Kalman Filtering

## Future Improvements

* Multi-object tracking.
* Acceleration-based motion models.
* Conversion of pixel velocity to real-world units.
* Automatic target identification among multiple bright objects.
* Trajectory prediction and orbital analysis.

## Conclusion

This project demonstrates the application of computer vision and Kalman filtering techniques for reliable satellite tracking. By combining image processing with state estimation, the system can accurately track object motion and estimate velocity from video data while mitigating measurement noise.

