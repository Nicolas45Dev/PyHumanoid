import numpy as np
import matplotlib.pyplot as plt

# foot_first 0 == left 1 == rig
def zmp_y_trajectory(foot_first : int = 0, dy : float = 0.037, n_step : int = 0):
    dt = 1
    init_step_time = 1 * dt

    #count = (3 + (n_step-1)*2) + 1
    count = n_step*2
    trajectory_initial = np.zeros((3,2))            # 3 points
    trajectory_normal = np.zeros((count, 2))   # 3 points * n_step
    trajectory_end = np.zeros((3,2))                # 3 points

    # Y axis
    trajectory_initial[0][0] = 0
    trajectory_initial[0][1] = 0

    trajectory_initial[1][0] = 0
    trajectory_initial[1][1] = init_step_time

    trajectory_initial[2][0] = dy if foot_first == 0 else -dy
    trajectory_initial[2][1] = trajectory_initial[1][1] + dt

    # Time axis
    for i in range(count):
        if i == 0:
            trajectory_normal[i][0] = trajectory_initial[-1][0]
            trajectory_normal[i][1] = trajectory_initial[-1][1] + (4*dt)
        elif i % 2 == 1:
            trajectory_normal[i][0] = -trajectory_normal[i-1][0]
            trajectory_normal[i][1] = trajectory_normal[i-1][1] + dt
        else:
            trajectory_normal[i][0] = trajectory_normal[i-1][0]
            trajectory_normal[i][1] = trajectory_normal[i-1][1] + (4*dt)

    trajectory_end[0][0] = trajectory_normal[-1][0]
    trajectory_end[0][1] = trajectory_normal[-1][1] + (4*dt)

    trajectory_end[1][0] = 0
    trajectory_end[1][1] = trajectory_end[0][1] + dt

    trajectory_end[2][0] = 0
    trajectory_end[2][1] = trajectory_end[1][1] + (4*dt)
    trajectory = np.concatenate((trajectory_initial, trajectory_normal, trajectory_end), axis=0)

    plt.figure()
    # plt.plot(trajectory_initial[:,1],trajectory_initial[:,0], '-', label="Initial Curve", color='blue')
    # plt.plot(trajectory_normal[:,1], trajectory_normal[:,0], '-', label="Normal Curve", color='red')
    # plt.plot(trajectory_end[:,1], trajectory_end[:,0], '-', label="End Curve", color='green')
    plt.plot(trajectory[:,1], trajectory[:,0], '-')
    plt.legend()
    plt.show()

    return trajectory

