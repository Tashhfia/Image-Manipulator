import numpy as np
import matplotlib.pyplot as plt
import copy
from skimage import io

class ImageManipulator():
    def __init__(self, url) -> None:
        self.image = io.imread(url)

    def showOriginalImage(self):
        plt.imshow(self.image)
        plt.show()
    
    def flip(self, axis):
        if axis == 0:    # flip horizontally, flip rows
            flipped_im = self.image[:, ::-1, :]
        elif axis == 1:     # flip vertically, flip columns
            flipped_im = self.image[::-1, :, :]
        else:
            print("Invalid axis value!")
            flipped_im = self.image

        return flipped_im
    


def main():
    im = ImageManipulator("https://i.pinimg.com/736x/8c/dc/a5/8cdca5e3979427241ae50537c9be932b.jpg")
    k = im.flip(0)
    plt.imshow(k)
    plt.show()

    #im.showOriginalImage()



if __name__ == "__main__":
    main()