import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


# x = np.linspace(-1, 1, 200)
# y = np.linspace(-1, 1, 200)
# X, Y = np.meshgrid(x, y)

# tube = np.zeros()

# Z = X + Y  # Example scalar field

# plt.imshow(Z, cmap='hot', interpolation='none', extent=[-1, 1, -1, 1])
# plt.colorbar()
# plt.title("Heatmap of Z")
# plt.show()


# Image dimensions
height, width = 300, 600
image = np.ones((height, width, 3))  # RGB white background

# Draw a vertical gradient to simulate a glass tube effect
for i in range(height):
    alpha = 0.9 - 0.7 * (abs(i - height // 2) / (height // 2))
    image[i, :, :] *= alpha

fig, ax = plt.subplots()
ax.imshow(image)

# Dynode parameters
n_dynodes = 8
dynode_width = 60
dynode_height = 10
spacing = width // (n_dynodes + 2)

from matplotlib.patches import Rectangle

for i in range(n_dynodes):
    x = spacing * (i + 1)
    y = height // 2 - dynode_height // 2 - ((-1)**i) * 30  # Zig-zag pattern
    dynode = Rectangle((x, y), dynode_width, dynode_height, color='skyblue', ec='black')
    ax.add_patch(dynode)

ax.set_title("2D Visualization of Photomultiplier Tube")
ax.axis('off')
plt.show()