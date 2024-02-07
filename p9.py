import cv2
import numpy as np

# Create a blank canvas
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Define background color
background_color = (90, 0, 0)  # Light blue color for the sky

grass_color=(0, 155, 0) # grass color

# Define the region to be colored
top_left = (0, 0)  # Coordinates of the top-left corner of the region
bottom_right = (800, 300)  # Coordinates of the bottom-right corner of the region

# Define the region to be colored
t_l = (0, 300)  # Coordinates of the top-left corner of the region
b_r = (800, 700)  # Coordinates of the bottom-right corner of the region


# Fill the selected region with the background color
canvas[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = background_color
canvas[t_l[1]:b_r[1], t_l[0]:b_r[0]] = grass_color

# Define runway color
runway_color = (100, 100, 100)  # Gray color for the runway

# Define cloud color
cloud_color = (255, 255, 255)  # White color for the clouds

# Initialize cloud positions
clouds = [(150, 100), (400, 80), (200, 50), (450, 120)]

# Add clouds
for cloud in clouds:
    cv2.ellipse(canvas, cloud, (30, 20), 0, 0, 360, cloud_color, -1)
    cv2.ellipse(canvas, cloud, (50, 30), 0, 0, 360, cloud_color, -1)

# Initialize cloud positions
clouds = [(150, 100), (400, 80), (200, 50), (450, 120)]

# Draw the runway
cv2.rectangle(canvas, (50, 250), (550, 300), runway_color, -1)

# Define building color
building_color = (60, 100, 200)  # Gray color for the buildings

# Initialize building positions
buildings = [(50, 50, 50, 200), (200, 80, 80, 170), (350, 160, 200, 90)]

# Define window color
window_color = (0, 255, 255)  # White color for the windows

# Initialize window size
window_size = 10

# Add buildings with windows
for building in buildings:
    # Draw the building
    cv2.rectangle(canvas, (building[0], building[1]), (building[0] +
                  building[2], building[1] + building[3]), building_color, -1)

    # Add windows
    for i in range(0, building[2], 30):
        for j in range(0, building[3], 30):
            window_x = building[0] + i + 5
            window_y = building[1] + j + 5
            cv2.rectangle(canvas, (window_x, window_y), (window_x +
                          window_size, window_y + window_size), window_color, -1)


# Define car color
car_color = (125, 16, 187)  # White color for the car

# Initialize car position
car_x, car_y = 100, 230

# Define car dimensions
car_width = 80
car_height = 40

# Define car speed
car_speed = 2

# Define wheel color
wheel_color = (0, 0, 0)  # Black color for the wheels

# Draw wheels
wheel_radius = 10
wheel1_center = (car_x + 20, car_y + car_height)
wheel2_center = (car_x + car_width - 20, car_y + car_height)

# Define car speed
wheel_speed = 2


# Main loop for the car movement
while True:
    # Clear the canvas
    canvas[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = background_color

    # Draw the runway
    cv2.rectangle(canvas, (0, 250), (600, 300), runway_color, -1)

    # Add clouds
    for cloud in clouds:
        cv2.ellipse(canvas, cloud, (30, 20), 0, 0, 360, cloud_color, -1)
        cv2.ellipse(canvas, cloud, (50, 30), 0, 0, 360, cloud_color, -1)

    # Draw the wheels
    cv2.circle(canvas, wheel1_center, wheel_radius, wheel_color, -1)
    cv2.circle(canvas, wheel2_center, wheel_radius, wheel_color, -1)

    # Add buildings with windows
    for building in buildings:
        # Draw the building
        cv2.rectangle(canvas, (building[0], building[1]), (
            building[0] + building[2], building[1] + building[3]), building_color, -1)

        # Add windows
        for i in range(0, building[2], 30):
            for j in range(0, building[3], 30):
                window_x = building[0] + i + 5
                window_y = building[1] + j + 5
                cv2.rectangle(canvas, (window_x, window_y), (window_x +
                              window_size, window_y + window_size), window_color, -1)

    # Update car position
    car_x += car_speed
    wheel1_center = (car_x + 20, car_y + car_height)
    wheel2_center = (car_x + car_width - 20, car_y + car_height)
    # Draw the car body
    cv2.rectangle(canvas, (car_x, car_y), (car_x + car_width,
                  car_y + car_height), car_color, -1)

    # Show the canvas
    cv2.imshow('Car on Runway', canvas)

    # Exit if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
