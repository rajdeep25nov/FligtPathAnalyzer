import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Load the flight trial data
data = np.genfromtxt('/Users/rajdeepjaiswal/Documents/2023-07-04-09-36-14-5325-NAVIGATION.csv', delimiter=",", dtype=None, names=True, encoding=None)

# Extract the relevant columns
longitude = data['LONGITUDE']
latitude = data['LATITUDE']
altitude = data['ALTITUDE']

# Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the scatter plot
scatter = ax.scatter([], [], [], c='red')

# Update function for the animation
def update(frame):
    # Clear previous frame
    scatter.remove()

    # Update scatter plot data
    scatter = ax.scatter(longitude[:frame], latitude[:frame], altitude[:frame], c='red')

    # Set plot limits
    ax.set_xlim(min(longitude), max(longitude))
    ax.set_ylim(min(latitude), max(latitude))
    ax.set_zlim(min(altitude), max(altitude))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(data), interval=200, blit=False)

# Show the plot
plt.show()
