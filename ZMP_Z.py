import numpy as np
import matplotlib.pyplot as plt


def zmp_z_trajectory(trajectory_x, trajectory_y, height=0.5):
    """
    Génère une trajectoire ZMP en z (fixe ou modifiée).

    Args:
        trajectory_x (np.ndarray): Points ZMP en x.
        trajectory_y (np.ndarray): Points ZMP en y.
        height (float): Hauteur constante du ZMP (en mètres).

    Returns:
        np.ndarray: Trajectoire ZMP avec x, y, z.
    """
    # Vérification que les dimensions de x et y correspondent
    if len(trajectory_x) != len(trajectory_y):
        raise ValueError("Les trajectoires en x et y doivent avoir la même longueur.")

    # Initialiser un tableau pour la trajectoire 3D (x, y, z)
    trajectory_z = np.zeros((len(trajectory_x), 3))

    # Remplir x, y, et définir z avec une hauteur constante
    trajectory_z[:, 0] = trajectory_x[:, 0]  # x
    trajectory_z[:, 1] = trajectory_y[:, 0]  # y
    trajectory_z[:, 2] = height  # z constant, peut être modifié si besoin

    # Exemple d'une modification dynamique de z en fonction de x et y
    # trajectory_z[:, 2] = height + 0.1 * np.sin(trajectory_z[:, 0])

    # Visualisation
    plt.figure()
    plt.plot(trajectory_z[:, 0], trajectory_z[:, 1], label="ZMP XY", color='blue')
    plt.scatter(trajectory_z[:, 0], trajectory_z[:, 2], label="ZMP Z", color='red')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.title("Trajectoire ZMP en Z")
    plt.show()

    return trajectory_z