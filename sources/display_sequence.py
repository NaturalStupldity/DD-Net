import os
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

root_datase = '../data/SHREC/'

idx_gesture = 1
idx_subject = 1
idx_finger = 1
idx_essai = 1

# Idx of the bones in the hand skeleton to display it.
bones = np.array([
    [0, 1],
    [0, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [1, 6],
    [6, 7],
    [7, 8],
    [8, 9],
    [1, 10],
    [10, 11],
    [11, 12],
    [12, 13],
    [1, 14],
    [14, 15],
    [15, 16],
    [16, 17],
    [1, 18],
    [18, 19],
    [19, 20],
    [20, 21]
])

# Path of the gesture
path_gesture = os.path.join(root_datase, f'gesture_{idx_gesture}/finger_{idx_finger}/subject_{idx_subject}/essai_{idx_essai}/')

if os.path.isdir(path_gesture):

    path_skeletons_image = os.path.join(path_gesture, 'skeletons_image.txt')

    skeletons_image = np.loadtxt(path_skeletons_image)

    pngDepthFiles = np.zeros([skeletons_image.shape[0], 480, 640])
    skeletons_display = np.zeros([skeletons_image.shape[0], 2, 2, 21])

    for id_image in range(skeletons_image.shape[0]):
        pngDepthFiles[id_image, :] = imageio.imread(os.path.join(path_gesture, f'{id_image}_depth.png'))

        x = np.zeros([2, bones.shape[0]])
        y = np.zeros([2, bones.shape[0]])

        ske = skeletons_image[id_image, :]

        for idx_bones in range(bones.shape[0]):
            joint1 = bones[idx_bones, 0]
            joint2 = bones[idx_bones, 1]

            pt1 = ske[joint1 * 2:joint1 * 2 + 2]
            pt2 = ske[joint2 * 2:joint2 * 2 + 2]

            x[0, idx_bones] = pt1[0]
            x[1, idx_bones] = pt2[0]
            y[0, idx_bones] = pt1[1]
            y[1, idx_bones] = pt2[1]

        skeletons_display[id_image, 0, :, :] = x
        skeletons_display[id_image, 1, :, :] = y

    for id_image in range(skeletons_image.shape[0]):
        plt.clf()
        plt.imshow(pngDepthFiles[id_image, :])
        plt.plot(skeletons_display[id_image, 0, :, :], skeletons_display[id_image, 1, :, :], linewidth=2.5)
        plt.pause(0.01)

else:
    print(f'There is no gesture in the path {path_gesture}')
