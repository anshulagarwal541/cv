import cv2
import numpy as np

# Create a 2D image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw different objects
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), -1)  # Blue rectangle
cv2.circle(image, (300, 100), 50, (0, 255, 0), -1)  # Green circle
cv2.line(image, (200, 200), (350, 350), (0, 0, 255), 2)  # Red line

# Display the original 2D image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
