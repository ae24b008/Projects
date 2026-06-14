import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, output_path):
    # Load the image in grayscale
    image = cv2.imread("Img2.png", cv2.IMREAD_GRAYSCALE)
    
    # Detect all non-black pixels (intensity > 0)
    non_black_pixels = np.column_stack(np.where(image > 0))
    
    # Convert grayscale image to BGR for coloring
    image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    # Mark all non-black pixels in red
    for y, x in non_black_pixels:
        image_colored[y, x] = [0, 0, 255]  # Red color (BGR)
    
    # Apply edge detection
    edges = cv2.Canny(image, 50, 150)
    
    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=10, minLineLength=10, maxLineGap=5)
    
    # Draw detected lines in green and print midpoints
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image_colored, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color (BGR)
            
            # Calculate midpoint
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            print(f"Midpoint of line from ({x1}, {y1}) to ({x2}, {y2}): ({mid_x}, {mid_y})")
    
    # Save the processed image
    cv2.imwrite("new.png", image_colored)
    
    # Display the image
    plt.figure(figsize=(5, 5))
    plt.imshow(cv2.cvtColor(image_colored, cv2.COLOR_BGR2RGB))
    plt.title("Non-Black Pixels (Red) & Detected Lines (Green)")
    plt.show()

# Example usage
input_image_path = "input_image.png"  # Replace with your image path
output_image_path = "output_image.png"
process_image(input_image_path, output_image_path)
