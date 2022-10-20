import base64
import logging
import cv2
import numpy as np

def base64_to_imagedata(im_b64):
    # PREPROCESS ORIGINAL IMAGE 
    try:
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))
        if type(img_bytes) == bytes:
            image_data = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), -1)

        return image_data

    except Exception as e:
        logging.error(f"Conversão da imagem base64. Falha ao recuperar a imagem.\n{e}")
        return None