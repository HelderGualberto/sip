import cv2

class ImgUtils:
    @staticmethod
    def to_RGB(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def to_grayscale(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def calc_rect_area(rect):
        return rect.h * rect.w