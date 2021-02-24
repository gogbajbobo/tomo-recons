# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk
import helper

# %%
shape = (100, 100)
image = np.zeros(shape)
_, _ = helper.process_image(image)

# %%
image = np.ones(shape)
recon_image, recon_image_sart = helper.process_image(image, with_fragment=True)

# %%
helper.plot_two_images(recon_image[:60, :20], recon_image_sart[:60, :20])

# %%
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
image = np.pad(image, 20)
recon_image, recon_image_sart = helper.process_image(image)

# %%
helper.plot_two_images(recon_image[51:147, 51:147], recon_image_sart[51:147, 51:147])

# %%
helper.plot_two_images(recon_image[:149, :47], recon_image_sart[:149, :47])

# %%
helper.plot_two_graphs(recon_image[99, :], recon_image_sart[99, :])

# %%
image = np.zeros(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 40)
image[rr, cc] = 1
recon_image, recon_image_sart = helper.process_image(image)

# %%
helper.plot_two_images(recon_image[46:96, 46:96], recon_image_sart[46:96, 46:96])

# %%
helper.plot_two_images(recon_image[:80, :30], recon_image_sart[:80, :30])

# %%
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 10)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 5)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 2)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 1)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//3), 5)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 5)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, shape[1]//3), 5)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, 2*shape[1]//3), 5)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 5)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, shape[1]//2-10), 5)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, shape[1]//2+10), 5)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
image = np.ones(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 1)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, shape[1]//2-2), 1)
image[rr, cc] = 0
rr, cc = disk((shape[0]//2, shape[1]//2+2), 1)
image[rr, cc] = 0
recon_image, recon_image_sart = helper.process_image(image)
helper.plot_two_images(image[40:61, 40:61], recon_image[61:82, 61:82])
helper.plot_two_images(image[40:61, 40:61], recon_image_sart[61:82, 61:82])
helper.plot_two_graphs(recon_image[71, :], recon_image_sart[71, :])

# %%
