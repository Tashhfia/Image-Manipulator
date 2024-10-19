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

def main():
    im = ImageManipulator("https://www.fau.de/files/2019/07/Kollegienhaus_Malter_3-480x284.jpg")
    im.showOriginalImage()


if __name__ == "__main__":
    main()