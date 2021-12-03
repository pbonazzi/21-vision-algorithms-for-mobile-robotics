import numpy as np


def poseVectorToTransformationMatrix(pose_vec):
    """ Converts a 6x1 pose vector into a 3x4 transformation matrix

    Parameters
    ----------
    pose_vec : [list] (ωx,ωy,ωz,tx,ty,tz) where ω is rotation, t is translation

    Returns
    -------
    RT : [array] transformation matrix

    """

    omega = pose_vec[:3]  # w
    t = pose_vec[3:]

    theta = np.linalg.norm(omega)  # ||w||=θ

    k = omega / theta

    k = np.around(k, 4)

    kx, ky, kz = k
    K = np.array([[0, -kz, ky], [kz, 0, -kx], [-ky, kx, 0]])

    R = np.eye(3) + K * np.sin(theta) + (1 - np.cos(theta)) * (np.dot(K, K))

    t = np.expand_dims(t, axis=-1)
    RT = np.concatenate((R, t), axis=1)

    return RT
