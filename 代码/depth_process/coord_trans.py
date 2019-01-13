import cv2
import numpy as np


def coord_transform(path, step=5, camera_fx=588.03, camera_fy=587.07):
    """将深度图像转化为三维点云

    Arguments:
        path {str} -- 深度图像的路径

    Keyword Arguments:
        step {int} -- 取点间隔 (default: {5})
        camera_fx {float} -- fx参数 (default: {588.03})
        camera_fy {float} -- fy参数 (default: {587.07})
    """
    depth = cv2.imread(path, -1)

    rows = len(depth)
    cols = len(depth[0])
    pointcloud = []

    for v in range(0, rows, step):
        for u in range(0, cols, step):
            # d = depth[m][n][0] + depth[m][n][1]*256
            z = float(depth[v][u])
            x = u * z / camera_fx
            y = v * z / camera_fy
            points = [x, y, z]
            if z <= 10 or z >= 25000:
                pass
            else:
                pointcloud.append(points)

    pointcloud = np.array(pointcloud, dtype=np.float32)
    return pointcloud


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    pointcloud = coord_transform("DepthToColour 91.png")
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(pointcloud[:, 0], pointcloud[:, 1], pointcloud[:, 2])
    ax.set_xlim([0, 25000])
    ax.set_ylim([0, 25000])
    ax.set_zlim([0, 30000])
    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()
