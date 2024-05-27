#3d object triangle

import csv
import chardet
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
    return encoding if encoding else 'utf-8'

def read_flight_data(file_path):
    encoding = detect_encoding(file_path)

    with open(file_path, 'r', encoding=encoding, errors='replace') as csv_file:
        reader = csv.DictReader(csv_file)
        header = reader.fieldnames

        latitude_list = []
        longitude_list = []
        altitude_list = []

        for row in reader:
            latitude = float(row.get('LATTITUDE', 0.0))
            longitude = float(row.get('LONGITUDE', 0.0))
            altitude = float(row.get('ALTITUDE(METERS)', 0.0))

            latitude_list.append(latitude)
            longitude_list.append(longitude)
            altitude_list.append(altitude)

    return latitude_list, longitude_list, altitude_list

# Example usage
file_path = '/Users/rajdeepjaiswal/Documents/2023-07-04-09-36-14-5325-NAVIGATION.csv'
latitude, longitude, altitude = read_flight_data(file_path)

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the initial flight path
scatter = ax.scatter(latitude[0], longitude[0], altitude[0], c='b', marker='o')

# Adding labels and title
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
ax.set_title('Flight Path Animation')

# Setting the initial triangle coordinates
triangle_coords = np.array([[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0, 0, 0]])

# Creating the triangle plot
triangle = ax.plot(triangle_coords[:, 0], triangle_coords[:, 1], triangle_coords[:, 2], c='r')

# Animation update function
def update(frame):
    # Update the flight path
    scatter._offsets3d = (latitude[:frame], longitude[:frame], altitude[:frame])

    # Rotate the triangle around the Z-axis
    angle = frame * 5  # Adjust the rotation speed as desired
    rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
                                [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
                                [0, 0, 1]])
    rotated_triangle = np.dot(triangle_coords, rotation_matrix.T)

    # Update the triangle plot
    triangle[0].set_data(rotated_triangle[:, 0], rotated_triangle[:, 1])
    triangle[0].set_3d_properties(rotated_triangle[:, 2])

    # Create an array of the same value for zs with the length of xs
    zs = np.full_like(latitude[:frame], altitude[0])

    return scatter, *triangle

# Creating the animation
animation = FuncAnimation(fig, update, frames=len(latitude), interval=50, blit=True)

# Displaying the animation
plt.show()
