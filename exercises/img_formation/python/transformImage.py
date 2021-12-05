import cv2 as cv
from PIL import Image
import numpy as np

def transformTogrey(directory, fname):

    """ Applies lens distortion D(2x1) to 2D points x(2xN) on the image plane.

    Parameters
    ----------
    - directory : [string] directory where to find the file
    - fname : [string] name of the file

    Returns
    -------
    newfname : [string] path to the grey version

    """

    img = Image.open(directory+fname).convert('LA')
    newfname = directory+"/grey" + fname[:-3]+"png"
    img.save(newfname)
    

    return newfname


def undistortImage(fnameG, K, D, dirU):
    """ Projects 3d points to the image plane (3xN), given the camera matrix (3x3) and
     distortion coefficients (2x1).

    Parameters
    ----------
    - fnameG : [string] path to grey image file
    - K : [array 3x3] camera matrix
    - D : [array 2x1] distortion coefficients
    - dirU : [string] path to undistorted folder

    """
    
    dist = np.array([*D, 0,0,0 ])
    img = cv.imread(fnameG)
    h,  w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(K, dist, (w,h), 1, (w,h))
    # undistort
    dst = cv.undistort(img, K, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    
    cv.imwrite(dirU+"/"+fnameG[-12:], dst)
    
    
    
    