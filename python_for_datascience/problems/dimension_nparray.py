import numpy as np

# Grayscale image
Image = np.array([[0, 255, 128],
                 [64, 32, 16]])

# Finding dimensions
dimension =Image.ndim

if dimension == 3:
    print("Colored Image")
elif dimension == 2:
    print("Grayscale Image")
else:
    pass