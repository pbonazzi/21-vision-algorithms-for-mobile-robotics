import numpy as np


def projectPoints(points_3d, K, D=np.zeros((4, 1))):
    """ Projects 3d points to the image plane (3xN), given the camera matrix (3x3) and
     distortion coefficients (2x1).

    Parameters
    ----------
    - points_3d : [array 3xn] 3d points
    - K : [array 3x3] camera matrix
    - D : [array 2x1] distortion coefficients

    Returns
    -------
    function : distortPoints(projected_points,D,K)

    """

    # get image coordinates
    projected_points = np.dot(K, points_3d)
    projected_points = projected_points / projected_points[2:]

    # apply distortion
    return distortPoints(projected_points, D, K)


def distortPoints(projected_points, D, K):

    """ Applies lens distortion D(2x1) to 2D points x(2xN) on the image plane.

    Parameters
    ----------
    - projected_points : [array 3xn] 3d camera points
    - K : [array 3x3] camera matrix
    - D : [array 2x1] distortion coefficients

    Returns
    -------
    xpp, ypp : tuple of [lists]

    """

    # distortion
    u0 = K[0][2]
    v0 = K[1][2]
    
    xp = projected_points[:1][0] - u0
    yp = projected_points[1:2][0] - v0

    d1, d2, p1, p2 = D
    
    r2 = xp*xp+ yp*yp
    m = (1 + d1 * r2 + d2 * r2 * r2)
    xpp = (xp * m + u0)
    ypp = (yp * m + v0)
    

    return xpp, ypp
