import numpy as np


def create_grid(square_size, num_corners_x, num_corners_y):
    """ Create a num_corners_x * num_corners_y grid , with a given square_size

    Parameters
    ----------
    square_size, num_corners_x, num_corners_y : 3x[int]

    Returns
    -------
    p_W_corners : [3 x num_corners array] world coordinates of grid points

    """

    num_corners = num_corners_x * num_corners_y

    # create a grid

    x = np.arange(0, num_corners_x, 1)
    y = np.arange(0, num_corners_y, 1)

    xx, yy = np.meshgrid(x, y, sparse=False)
    xx = np.reshape(xx, (1, -1), order='F')[0]
    yy = np.reshape(yy, (1, -1), order='F')[0]

    p_W_corners = square_size * np.vstack((xx, yy))
    zero = np.zeros((1, num_corners))
    p_W_corners = np.concatenate((p_W_corners, zero))  # add the z-axis
    return p_W_corners
