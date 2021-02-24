import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon, iradon_sart


def process_image(image, with_fragment=False):

    sinogram = radon(image, circle=False)
    print_min_max_shape(image, 'image')
    print_min_max_shape(sinogram, 'sinogram')
    plot_two_images(image, sinogram, 'image', 'sinogram')

    recon_image = iradon(sinogram)
    recon_image_sart = iradon_sart(sinogram)
    print_min_max_shape(recon_image, 'recon_image')
    print_min_max_shape(recon_image_sart, 'recon_image_sart')
    plot_two_images(recon_image, recon_image_sart, 'recon_image', 'recon_image_sart')

    if with_fragment:
        plot_two_images(
            recon_image[23:119, 23:119],
            recon_image_sart[23:119, 23:119],
            'recon_image fragment',
            'recon_image_sart  fragment'
        )

    return recon_image, recon_image_sart


def print_min_max_shape(image, title):
    print(f'{title} max {np.max(image)}, min {np.min(image)}, shape {image.shape}')


def plot_two_images(image0, image1, title0=None, title1=None):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    im0 = axes[0].imshow(image0)
    im1 = axes[1].imshow(image1)
    title0 and axes[0].title.set_text(title0)
    title1 and axes[1].title.set_text(title1)
    fig.colorbar(im0, ax=axes[0])
    fig.colorbar(im1, ax=axes[1])


def plot_two_graphs(x0, x1, title0=None, title1=None):
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    axes[0].plot(x0)
    axes[1].plot(x1)
    title0 and axes[0].title.set_text(title0)
    title1 and axes[1].title.set_text(title1)
