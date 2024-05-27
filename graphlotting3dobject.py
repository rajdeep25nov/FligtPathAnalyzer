import csv
import chardet
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
    return encoding

def read_flight_data(file_path):
    encoding = detect_encoding(file_path)

    with open(file_path, 'r', encoding=encoding) as csv_file:
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

# Plotting the flight path
ax.scatter(latitude, longitude, altitude, c='b', marker='o')

# Adding labels and title
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')
ax.set_title('Flight Path')

# Adding a simple 3D airplane object
# Replace with your own 3D airplane model if available
airplane = ax.plot([0], [0], [0], c='r', marker='^')  # Placeholder for airplane object

# Displaying the plot
plt.show()
