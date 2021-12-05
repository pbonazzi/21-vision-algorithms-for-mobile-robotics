import cv2 as cv
import numpy as np


def estimatePoseVectorDLT(p_W_corners, p_C_corners, K, D=np.array([0, 0, 0, 0])):
    """ Estimates object pose given

    Parameters
    ----------
    - p_W_corners : [array Nx3]
    - p_C_corners : [array Nx2]
    - K : [array 3x3] camera matrix
    - D : [array 2x1] distortion coefficients

    Return
    ----------
    - pose_vec : [list] (ωx,ωy,ωz,tx,ty,tz) where ω is rotation, t is translation

    Documentation
    ----------
    https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga549c2075fac14829ff4a58bc931c033d

    """

    ret, R, t = cv.solvePnP(p_W_corners, p_C_corners, K, D)

    return np.array([*R.reshape(-1), *t.reshape(-1)])
