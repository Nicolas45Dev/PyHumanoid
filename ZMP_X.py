import numpy as np
import matplotlib.pyplot as plt

def zmp_x_trajectory(zmp_y, dx : int  = 0.1):
    # Create a nparray with the same shape as xmp_y
    zmp_x = np.copy(zmp_y)
    # Clone
    zmp_x[0][0] = 0
    zmp_x[1][0] = 0
    zmp_x[2][0] = dx
    for i in range(3, len(zmp_x)):
        if i % 2 == 0:
            # bouge
            zmp_x[i][0] = zmp_x[i-1][0] + 2 * dx
        else:
            #pas bouge
            zmp_x[i][0] = zmp_x[i-1][0]

    plt.figure()
    plt.plot(zmp_x[:,1],zmp_x[:,0], '-', label="Initial Curve", color='blue')
    plt.legend()
    plt.show()

    return zmp_x