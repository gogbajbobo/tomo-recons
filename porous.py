# Нужны следующие пакеты:
# porespy — https://porespy.readthedocs.io
# numpy — https://numpy.org
# matplotlib — https://matplotlib.org
# skimage — https://scikit-image.org

import os
import porespy as ps
import numpy as np
import matplotlib.pyplot as plt
import skimage.transform as skt


def generate_images(blobiness):

    # Генератор пористой структуры
    # https://porespy.readthedocs.io/en/master/modules/generators.html#porespy.generators.blobs
    # '~' — для инвертирования картинки, чтобы материал был 1, а поры — 0
    # blobiness по документации должен быть int, но float тоже проходит без ошибок

    porous_image = ~ps.generators.blobs(shape=[700, 700], porosity=0.3, blobiness=blobiness)
    fig1 = plt.figure()
    plt.imshow(porous_image)

    # Расчёт синограммы
    # https://scikit-image.org/docs/stable/api/skimage.transform.html#skimage.transform.radon

    porous_sinogram = skt.radon(porous_image, circle=False)
    fig2 = plt.figure()
    ax = fig2.add_subplot()
    ax.imshow(porous_sinogram)
    ax.set_aspect(0.1)

    # Сохраняем всё в файлы
    # https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html?highlight=savefig#matplotlib.pyplot.savefig
    # Под Windows path будет выглядеть как-то так: 'D:\tmp'

    path = '/Users/grimax/Desktop/tmp'
    image_path = os.path.join(path, f'porous_image_{blobiness}.dat')
    sinogram_path = os.path.join(path, f'porous_sinogram_{blobiness}.dat')
    image_png_path = os.path.join(path, f'porous_image_{blobiness}.png')
    sinogram_png_path = os.path.join(path, f'porous_sinogram_{blobiness}.png')

    np.savetxt(image_path, porous_image, fmt='%d')
    np.savetxt(sinogram_path, porous_sinogram, fmt='%d')
    fig1.savefig(image_png_path)
    fig2.savefig(sinogram_png_path)


# Генерим и сохраняем 4 пористых объекта с разным blobiness

for b in [0.5, 1, 2, 4]:
    generate_images(b)

plt.show()
