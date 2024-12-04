import numpy as np
from ZMP_X import zmp_x_trajectory
from ZMP_Y import zmp_y_trajectory
from ZMP_Z import zmp_z_trajectory
from CoM import com_trajectory
from Interpolation import interpolate_points
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Faire la matrice des pas
    #matrix = [[1, 0, 0.5],[2, 0.1, 0.5],[3, 0.1, 0.5],[4, 0.1, 0.5],[5, 0, 0.5]]


    xmp_y = zmp_y_trajectory(0, 0.037, 6)
    zmp_x = zmp_x_trajectory(xmp_y, 0.1)
    zmp_3d = zmp_z_trajectory(zmp_x, xmp_y, 0.45)
    com_traj = com_trajectory(zmp_3d, h=0.45, dt=0.01, total_time=5.0)

    plt.figure()
    plt.plot(com_traj[:, 0], com_traj[:, 1], label="CoM Trajectory")
    plt.plot(zmp_3d[:, 0], zmp_3d[:, 1], label="ZMP Trajectory", linestyle='--')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectoire CoM vs ZMP")
    plt.grid()
    plt.show()

    #
    #
    # # Create information here
    # xmp_y_interpolate = interpolate_points(xmp_y, method='linear', num_points=1000)
    # zmp_x_interpolate = interpolate_points(zmp_x, method='linear', num_points=1000)
    #
    # print(len(xmp_y_interpolate[0]))
    # print(len(zmp_x_interpolate[0]))
    #
    # # Plot the interpolated curves
    # plt.figure()
    # plt.plot(*xmp_y_interpolate, '-', label="ZMP Y")
    # #plt.plot(*zmp_x, '-', label="ZMP X")
    # plt.legend()
    # plt.show()
