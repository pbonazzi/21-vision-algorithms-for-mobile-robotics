import numpy as np


def create_grid(square_size, num_corners_x, num_corners_y):
    """ Create a num_corners_x * num_corners_y grid , with a given square_size

    Parameters
    ----------
    square_size,  : [float]
    num_corners_x, num_corners_y : [int]

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


def create_cube(square_size, offset_x, offset_y):
    """ Create a num_corners_x * num_corners_y grid , with a given square_size

    Parameters
    ----------
    square_size, offset_x, offset_y : 3x[float]

    Returns
    -------
    p_W_corners : [3 x num_corners array] world coordinates of grid points

    """

    # create a grid

    x = np.arange(0, 2, 1)
    y = np.arange(0, 2, 1)
    z = np.arange(0, 2, 1)

    xx, yy, zz = np.meshgrid(x, y, z, sparse=False)
    xx = np.reshape(xx, (1, -1), order='F')[0]
    yy = np.reshape(yy, (1, -1), order='F')[0]
    zz = np.reshape(zz, (1, -1), order='F')[0]

    p_W_corners = square_size * np.vstack((xx, yy, zz))
    p_W_corners[0] =p_W_corners[0] +offset_x
    p_W_corners[1] =p_W_corners[1] +offset_y
   
    return p_W_corners



def plot_cube(square_size, offset_x, offset_y):
    """ Create a num_corners_x * num_corners_y grid , with a given square_size

    Parameters
    ----------
    square_size, offset_x, offset_y : 3x[float]

    Returns
    -------
    p_W_corners : [3 x num_corners array] world coordinates of grid points

    """

    # create a grid

    x = np.arange(0, 2, 1)
    y = np.arange(0, 2, 1)
    z = np.arange(0, 2, 1)

    xx, yy, zz = np.meshgrid(x, y, z, sparse=False)
    xx = np.reshape(xx, (1, -1), order='F')[0]
    yy = np.reshape(yy, (1, -1), order='F')[0]
    zz = np.reshape(zz, (1, -1), order='F')[0]

    p_W_corners = square_size * np.vstack((xx, yy, zz))
    p_W_corners[0] =p_W_corners[0] +offset_x
    p_W_corners[1] =p_W_corners[1] +offset_y
   
    return p_W_corners