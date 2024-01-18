class ImageBase64:

    def __init__(self):
        pass

    def get_header_of_base64_image(base64_image: str) -> str:
        return base64_image[:base64_image.find(',') + 1]


    def get_extension_from_base64_image(base64_image: str, extensions: list(str)) -> str:
        header = get_header_of_base64_image(base64_image)
        for extension in extensions:
            if extension in header:
                return extension


    def remove_header_from_base64_image(base64_image: str) -> str:
        header = get_header_of_base64_image(base64_image)
        return base64_image.replace(header, "")


    def validate_image_header(header: str, extensions: list(str)) -> bool:
        return  any(extension in header for extension in extensions)
