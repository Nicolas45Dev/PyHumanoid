import numpy as np
import matplotlib.pyplot as plt

def com_trajectory(zmp_trajectory, h=0.5, dt=0.01, total_time=5.0):
    """
    Calcule la trajectoire du Centre de Masse (CoM) à partir de la trajectoire ZMP.

    Args:
        zmp_trajectory (np.ndarray): Trajectoire ZMP (x, y, z) ou (x, y).
        h (float): Hauteur du pendule inversé (CoM par rapport au ZMP).
        dt (float): Pas de temps pour l'intégration.
        total_time (float): Durée totale de la simulation (en secondes).

    Returns:
        np.ndarray: Trajectoire CoM (x, y, z).
    """
    g = 9.81  # Accélération gravitationnelle
    omega = np.sqrt(g / h)  # Fréquence naturelle
    t_steps = int(total_time / dt)

    # Initialisation des trajectoires CoM
    com_trajectory = np.zeros((t_steps, 3))
    zmp_trajectory_resampled = np.interp(
        np.linspace(0, total_time, t_steps),
        np.linspace(0, total_time, len(zmp_trajectory)),
        zmp_trajectory[:, :2].T
    ).T

    # Conditions initiales (CoM commence sur le ZMP)
    com_trajectory[0, :2] = zmp_trajectory[0, :2]
    com_velocity = np.zeros(2)  # Vitesse initiale du CoM

    # Calcul du CoM par intégration
    for i in range(1, t_steps):
        zmp_current = zmp_trajectory_resampled[i]
        delta_accel = omega ** 2 * (com_trajectory[i-1, :2] - zmp_current)
        com_velocity += -delta_accel * dt
        com_trajectory[i, :2] = com_trajectory[i-1, :2] + com_velocity * dt

    # Si le ZMP contient une composante z, l'ajouter au CoM
    if zmp_trajectory.shape[1] == 3:
        com_trajectory[:, 2] = zmp_trajectory[:, 2]

    return com_trajectory
