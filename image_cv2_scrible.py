import numpy as np
import cv2


class Image:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path)
        self.shape = self.image.shape[:2][::-1]  # width, height must be given
        self.height = self.shape[0]
        self.width = self.shape[1]

    def scale(self, fx: float, fy: float) -> None:
        self.image = cv2.resize(self.image, (0, 0), fx=fx, fy=fy)

    def resize(self, dimensions: tuple) -> None:
        self.image = cv2.resize(self.image, dimensions)

    def rotate_90_clockwise(self) -> None:
        self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_CLOCKWISE)

    def rotate_90_anticlockwise(self) -> None:
        self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

    def rotate_180(self) -> None:
        self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_180)

    def copy(self) -> any:
        return self.image.copy()

    def replace_patch(self, target: list, patch: any) -> None:
        [height, width] = patch.shape
        x1, x2 = target[0]
        y1, y2 = target[1]

        if (x2-x1 != width) or (y2-y1 != height):
            raise Exception("Patch does not match target dimensions")

        if (x1 < 0) or (x2 >= self.width) or (y1 < 0) or (y2 >= self.height):
            raise Exception("Dimensions out of bounds")

        self.image[x1: x2, y1: y2] = patch

    def select_patch(self, start_pos: tuple, end_pos: tuple):
        x1, y1 = start_pos
        x2, y2 = end_pos
        selected_region = self.image[x1:x2, y1:y2]
        return selected_region

    def show(self) -> None:
        cv2.imshow("frame", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


snf = Image('test_images/sunflower_900_600.jpeg')
print('1')
snf.scale(300, 200)
print('2')
snf.show()
