import matplotlib.pyplot as plt
import random

# Create a sample image (a simple 2D array)
grid_size = 10
image = image = [[random.random() for _ in range(grid_size)] for _ in range(grid_size)]

# Display the image
plt.imshow(image, cmap="terrain")
plt.title("Click on the image")

# Use ginput to get any number of points
print("Left-Click on the image to add a point")
print("Right-Click to undo the last point")
print("Middle-Click to finish")
coordinates = plt.ginput(n=-1, timeout=0)
plt.close()

# print output
[
    print(f"Point {index}: ({value[0]:.2f}, {value[1]:.2f})")
    for index, value in enumerate(coordinates)
]
