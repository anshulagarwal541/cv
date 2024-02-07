import cv2
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread('C:\\Users\\LENOVO\\Downloads\\wallpix1563792248-above-aerial-aerial-view-931018.jpg')  # Replace 'your_image.jpg' with the path to your image

# Convert BGR to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and converted images
plt.subplot(131), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(133), plt.imshow(gray_image, cmap='gray'), plt.title('Grayscale')
plt.show()
