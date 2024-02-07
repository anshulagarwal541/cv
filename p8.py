import cv2
import numpy as np
from math import cos, sin


def draw_cube(vertices, edges, colors, angle_x, angle_y, angle_z, scale_factor):
    # Create a 3D rotation matrix for each axis
    rotation_x = np.array([[1, 0, 0],
                           [0, cos(angle_x), -sin(angle_x)],
                           [0, sin(angle_x), cos(angle_x)]])

    rotation_y = np.array([[cos(angle_y), 0, sin(angle_y)],
                           [0, 1, 0],
                           [-sin(angle_y), 0, cos(angle_y)]])

    rotation_z = np.array([[cos(angle_z), -sin(angle_z), 0],
                           [sin(angle_z), cos(angle_z), 0],
                           [0, 0, 1]])

    # Combine rotation matrices
    rotation_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))

    # Rotate and scale vertices
    rotated_scaled_vertices = scale_factor * \
        np.dot(rotation_matrix, vertices.T).T

    # Project 3D points to 2D
    projection_matrix = np.array([[1, 0, 0],
                                  [0, 1, 0]])

    projected_vertices = np.dot(projection_matrix, rotated_scaled_vertices.T).T

    # Translate the 2D points to the center of the image
    translated_vertices = projected_vertices + np.array([300, 300])

    # Create an empty black image
    image = np.zeros((600, 600, 3), dtype=np.uint8)

    # Draw edges
    for edge in edges:
        start_point = tuple(translated_vertices[edge[0]].astype(int))
        end_point = tuple(translated_vertices[edge[1]].astype(int))
        color = colors[edge[0]]
        cv2.line(image, start_point, end_point, color, 2)

    return image


def main():
    # Define cube vertices, edges, and colors
    vertices = np.array([[-1, -1, -1],
                         [-1, 1, -1],
                         [1, 1, -1],
                         [1, -1, -1],
                         [-1, -1, 1],
                         [-1, 1, 1],
                         [1, 1, 1],
                         [1, -1, 1]])

    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),
              (255, 255, 0), (255, 0, 255), (0, 255, 255),
              (128, 128, 128), (255, 255, 255)]

    # Initialize rotation angles and scale factor
    angle_x = 0
    angle_y = 0
    angle_z = 0
    scale_factor = 100  # Adjust this value to change the size of the cube

    while True:
        # Draw and display the cube with rotation and scaling
        image = draw_cube(vertices, edges, colors, angle_x,
                          angle_y, angle_z, scale_factor)
        cv2.imshow('Rotating Cube', image)

        # Update rotation angles
        angle_x += 0.01
        angle_y += 0.02
        angle_z += 0.03

        # Break the loop if 'Esc' key is pressed
        if cv2.waitKey(30) == 27:
            break


cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
