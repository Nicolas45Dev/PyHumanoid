import numpy as np
from scipy.interpolate import interp1d, splprep, splev
import matplotlib.pyplot as plt

def interpolate_points(points, method='linear', num_points=100):
    """
    Interpolate between a list of points using the specified method.

    Parameters:
        points (list of tuple): List of (x, y) points to interpolate.
        method (str): Interpolation method ('linear', 'quadratic', 'cubic', 'spline').
        num_points (int): Number of points in the interpolated result.

    Returns:
        tuple: Interpolated x and y values as numpy arrays.
    """
    points = np.array(points)
    x, y = points[:, 1], points[:, 0]

    if method in ['linear', 'quadratic', 'cubic']:
        # Interpolation using scipy's interp1d
        interp_func = interp1d(x, y, kind=method, fill_value="extrapolate")
        x_new = np.linspace(x.min(), x.max(), num_points)
        y_new = interp_func(x_new)
    elif method == 'spline':
        # Spline interpolation with smoothing using splprep/splev
        tck, _ = splprep([x, y], s=0)
        u_new = np.linspace(0, 1, num_points)
        x_new, y_new = splev(u_new, tck)
    else:
        raise ValueError("Invalid method. Choose 'linear', 'quadratic', 'cubic', or 'spline'.")

    return np.array(x_new), np.array(y_new)

# Example usage
if __name__ == "__main__":
    points = [(0, 0), (1, 2), (2, 0), (3, 3), (4, 1)]
    x_new, y_new = interpolate_points(points, method='spline', num_points=200)

    # Plot original points and interpolation
    plt.plot(*zip(*points), 'o', label="Original Points")
    plt.plot(x_new, y_new, '-', label="Interpolated Curve")
    plt.legend()
    plt.show()
