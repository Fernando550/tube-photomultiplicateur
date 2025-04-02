import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

tube = np.zeros()

Z = X + Y  # Example scalar field

plt.imshow(Z, cmap='hot', interpolation='none', extent=[-1, 1, -1, 1])
plt.colorbar()
plt.title("Heatmap of Z")
plt.show()