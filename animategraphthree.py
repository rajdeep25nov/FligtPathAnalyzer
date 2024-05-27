import csv
import chardet
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

        time_list = []
        roll_list = []
        pitch_list = []
        true_heading_list = []
        longitude_list = []
        latitude_list = []
        altitude_list = []

        for row in reader:
            time = float(row.get('TIME', 0.0))
            roll = float(row.get('ROLL(DEG)', 0.0))
            pitch = float(row.get('PITCH(DEG)', 0.0))
            true_heading = float(row.get('TRUE HEADING(DEG)', 0.0))
            longitude = float(row.get('LONGITUDE', 0.0))
            latitude = float(row.get('LATITUDE', 0.0))
            altitude = float(row.get('ALTITUDE(METERS)', 0.0))

            time_list.append(time)
            roll_list.append(roll)
            pitch_list.append(pitch)
            true_heading_list.append(true_heading)
            longitude_list.append(longitude)
            latitude_list.append(latitude)
            altitude_list.append(altitude)

    return time_list, roll_list, pitch_list, true_heading_list, longitude_list, latitude_list, altitude_list


file_path = '/Users/rajdeepjaiswal/Documents/2023-07-04-09-36-14-5325-NAVIGATION.csv'
time, roll, pitch, true_heading, longitude, latitude, altitude = read_flight_data(file_path)


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslate(0.0, 0.0, -5)


running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set the camera
    glRotatef(pitch[frame], 1, 0, 0)
    glRotatef(roll[frame], 0, 1, 0)
    glRotatef(true_heading[frame], 0, 0, 1)
    glTranslate(-longitude[frame], -latitude[frame], -altitude[frame])

    # Render
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glEnd()

    # Update the frame
    frame += 1
    if frame >= len(time):
        frame = 0

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
