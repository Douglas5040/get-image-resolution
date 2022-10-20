from tkinter import image_names
from utils import base64_to_imagedata

class ImageResolutionController:
    """
    """
    def __init__(self) -> None:
        pass

    def get_resolution(self, image_data):
        
        img_np = base64_to_imagedata(image_data)
        print("image shape --> ", img_np.shape)
        if not img_np.any():
            return None, None
        print("image shape --> ", img_np.shape)

        return img_np.shape[0], img_np.shape[1]