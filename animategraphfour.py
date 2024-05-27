#3d visualization


import csv
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_flight_data(file_path):
    time_list = []
    roll_list = []
    pitch_list = []
    true_heading_list = []
    longitude_list = []
    latitude_list = []
    altitude_list = []

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            time_str = row['TIME']
            time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S:%f')
            time_ms = time_obj.timestamp() * 1000.0
            time_list.append(time_ms)

            roll_list.append(float(row['ROLL(DEG)']))
            pitch_list.append(float(row['PITCH(DEG)']))
            true_heading_list.append(float(row['TRUE HEADING(DEG)']))
            longitude_list.append(float(row['LONGITUDE']))
            latitude_list.append(float(row['LATTITUDE']))
            altitude_list.append(float(row['ALTITUDE(METERS)']))

    return time_list, roll_list, pitch_list, true_heading_list, longitude_list, latitude_list, altitude_list

def plot_flight_path(time, latitude, longitude, altitude):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(longitude, latitude, altitude, marker='o')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Altitude')
    ax.set_title('Flight Path Visualization')

    plt.show()

# Example usage
file_path = '/Users/rajdeepjaiswal/Documents/2023-07-04-09-36-14-5325-NAVIGATION.csv'
time, roll, pitch, true_heading, longitude, latitude, altitude = read_flight_data(file_path)
plot_flight_path(time, latitude, longitude, altitude)
