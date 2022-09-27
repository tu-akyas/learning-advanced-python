import numpy as np
from PIL import Image


class Canvas:
    """
    Creating a canvas object on which shapes will be drawn
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Creating a 3d numpy array for the canvas page
        self.page_data = np.zeros([self.height, self.width, 3], dtype=np.uint8)

        # Change the colour of canvas page
        self.page_data[:] = self.color

    def create(self, path):
        img = Image.fromarray(self.page_data, 'RGB')
        img.save(path)
        img.show()