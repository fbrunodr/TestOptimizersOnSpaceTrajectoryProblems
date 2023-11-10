import numpy as np
import matplotlib.pyplot as plt
from objective_functions import jupiter1_single_objective


if __name__ == '__main__':
    # Create a grid of values within the specified range
    x_values = np.linspace(9131.5, 9495.5, 300)
    y_values = np.linspace(300, 3000, 300)
    x, y = np.meshgrid(x_values, y_values)
    z = np.array([jupiter1_single_objective([x_i, y_i]) for x_i, y_i in zip(np.ravel(x), np.ravel(y))])
    z = z.reshape(x.shape)
    # Plot the heatmap
    plt.figure(figsize=(6, 5))
    contour = plt.contourf(x, y, z, 50, cmap='turbo')
    cbar = plt.colorbar(contour)
    cbar.ax.set_title('$\Delta v$')
    plt.title('Heatmap of the Function Jupiter Easy')
    plt.xlabel('$T_0$')
    plt.ylabel('$\Delta T_1$')
    plt.show()
