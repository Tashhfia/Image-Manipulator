import numpy as np
import matplotlib.pyplot as plt
import copy
from skimage import io

class Preprocess():
    def __init__(self, url) -> None:
        self.image = io.imread(url)

    def showOriginalImage(self):
        plt.imshow(self.image)
        plt.show()
    
    def flip(self, axis):
        """ Takes in the image and the axis as arguements"""
        if axis == 0:    # flip horizontally, flip rows
            flipped_im = self.image[:, ::-1, :]
        elif axis == 1:     # flip vertically, flip columns
            flipped_im = self.image[::-1, :, :]
        else:
            print("Invalid axis value!")
            flipped_im = self.image
        return flipped_im
    
    def crop(self, x, y, width, height):
        """ Crops the image to a specified rectangular region.

        Parameters:
        x (int): The x-coordinate (column) of the top-left corner of the crop region.
        y (int): The y-coordinate (row) of the top-left corner of the crop region.
        width (int): The width of the crop region.
        height (int): The height of the crop region.

        Returns: The cropped portion of the image as a NumPy array."""

        im_w = self.image.shape[1]  # columns dictate the width so we take the second element of shape
        im_h = self.image.shape[0]  # rows dictate the height so we take the first element of shape
        print(f"width is {im_w}")

        if x >= im_w or y >= im_h:
            raise ValueError(f"x ({x}) or y ({y}) are out of image bounds (width: {im_w}, height: {im_h}).")
            
        # ensuring the values are within bounds
        x = max(0, min(x, im_w))  
        y = max(0, min(y, im_h))  
        crop_width = min(width, im_w - x)
        crop_height = min(height, im_h - y)

        # When slicing a NumPy image:
        # First value (before the first comma): Controls height (rows, y).
        # Second value (after the first comma): Controls width (columns, x).
        cropped = self.image[y:(y + crop_height), x: (x + crop_width), :]
        return cropped


    


def main():
    im = Preprocess("https://i.pinimg.com/736x/8c/dc/a5/8cdca5e3979427241ae50537c9be932b.jpg")


    #im.showOriginalImage()



if __name__ == "__main__":
    main()