import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread('C:\\Users\\LENOVO\\Downloads\\piron-guillaume-cRRDzGxqVe8-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Define a kernel(structuring element)
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size of the kernel

# Erosion
erosion = cv2.erode(image, kernel, iterations = 1)

# Dilation
dilation = cv2.dilate(image, kernel, iterations = 1)

# Display the original, eroded, and dilated images
plt.subplot(131), plt.imshow(image), plt.title('Original')
plt.subplot(132), plt.imshow(erosion), plt.title('Erosion')
plt.subplot(133), plt.imshow(dilation), plt.title('Dilation')
plt.show()
