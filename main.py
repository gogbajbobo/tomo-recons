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
from skimage.draw import disk
import helper

# %%
shape = (100, 100)
image = np.zeros(shape)
helper.process_image(image)

# %%
image = np.ones(shape)
recon_image, recon_image_sart = helper.process_image(image, with_fragment=True)

# %%
helper.plot_two_images(recon_image[:20, :20], recon_image_sart[:20, :20])

# %%
image = np.ones(shape)
image = np.pad(image, 20)
recon_image, recon_image_sart = helper.process_image(image)

# %%
helper.plot_two_images(recon_image[51:147, 51:147], recon_image_sart[51:147, 51:147])

# %%
helper.plot_two_images(recon_image[:49, :49], recon_image_sart[:49, :49])

# %%
image = np.zeros(shape)
rr, cc = disk((shape[0]//2, shape[1]//2), 40)
image[rr, cc] = 1
recon_image, recon_image_sart = helper.process_image(image)

# %%
helper.plot_two_images(recon_image[46:96, 46:96], recon_image_sart[46:96, 46:96])

# %%
helper.plot_two_images(recon_image[:40, :40], recon_image_sart[:40, :40])

# %%
