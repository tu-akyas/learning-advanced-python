import numpy as np
from PIL import Image

# Create a 3d numpy array of zeros and then replace zeros(black pixels) with yellow pixel
data = np.zeros(shape=(5, 4, 3), dtype=np.uint8)

# Access all elements in data array
data[:] = [255, 255, 0]


# Access part of data and add a Red Patch
data[1:3] = [255, 0, 0]
data[:, 1:3] = [0, 255, 0]

print(data)
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
