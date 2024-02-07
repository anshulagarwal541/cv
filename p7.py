import numpy as np
import cv2

width = 400
height = 300
img = np.zeros((height, width, 3), np.uint8)
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

color = (255, 0, 0)  # Initial color is blue

def draw_triangle():
    cv2.line(img, p1, p2, color, 3)
    cv2.line(img, p2, p3, color, 3)
    cv2.line(img, p1, p3, color, 3)

def calculate_centroid():
    return ((p1[0]+p2[0]+p3[0])//3, (p1[1]+p2[1]+p3[1])//3)

def draw_centroid(centroid):
    cv2.circle(img, centroid, 4, (0, 255, 0))

def change_color(event, x, y, flags, param):
    global color

    if event == cv2.EVENT_LBUTTONDOWN:
        # Change color to a random color on left mouse button click
        color = tuple(np.random.randint(0, 256, 3).tolist())
        draw_triangle()
        centroid = calculate_centroid()
        draw_centroid(centroid)
        cv2.imshow("image", img)

cv2.namedWindow("image")
cv2.setMouseCallback("image", change_color)

while True:
    draw_triangle()
    centroid = calculate_centroid()
    draw_centroid(centroid)
    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()
