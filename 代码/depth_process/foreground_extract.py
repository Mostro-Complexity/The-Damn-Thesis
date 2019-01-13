import cv2
import numpy as np


if __name__ == "__main__":

    img = cv2.imread('DepthToColour 91.png', -1)
    # mask = np.zeros(img.shape[:2], np.uint8)
    # bgdModel = np.zeros((1, 65), np.float64)
    # fgdModel = np.zeros((1, 65), np.float64)
    # rect = (10, 10, img.shape[1] - 10, img.shape[0] - 10)
    # cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    cv2.imshow('original image', img)
    img[np.logical_or(img > 23500, img < 17000)] = 0
    cv2.imshow('human part', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

