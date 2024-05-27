
#not working
import csv
import chardet
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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
            latitude = float(row.get('latitude', 0.0))
            longitude = float(row.get('longitude', 0.0))
            altitude = float(row.get('altitude', 0.0))

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

# Plotting the flight path
scatter = ax.scatter(latitude, longitude, altitude, c='b', marker='o')

# Adding labels and title
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
ax.set_title('Flight Path Animation')

# Create a pointer or object
pointer = ax.plot([latitude[0]], [longitude[0]], [altitude[0]], marker='o', markersize=10, c='r')[0]

# Animation update function
def update(frame):
    # Update the flight path
    scatter._offsets3d = (latitude[:frame], longitude[:frame], altitude[:frame])

    # Update the pointer position
    pointer.set_data_3d(latitude[frame], longitude[frame], altitude[frame])

# Creating the animation
animation = FuncAnimation(fig, update, frames=len(latitude), interval=50)

# Display the plot
plt.show()
