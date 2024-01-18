import base64Image
import io
import cv2
import numpy as np
from PIL import Image

class Images:

    NUMBER_OF_COLOR_CHANNELS = 3

    def __init__(self):
        pass

    def base64_to_ndarray(base64_image: str) -> np.ndarray:
        base64_decoded = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(base64_decoded))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, settings.image_size)

        return image

    def ndarray_to_base64(ndarray_image: np.ndarray, extension: str) -> str:
        success, encoded_image = cv2.imencode(f".{extension}", ndarray_image)

        return base64.b64encode(encoded_image.tobytes()).decode("utf-8")

    def cv2_to_image(img: np.ndarray) -> Image:
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    def image_to_cv2(img: Image) -> np.ndarray:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
