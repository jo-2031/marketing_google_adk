import base64

def encode_image_to_base64(image_path: str) -> str:
    """Encodes an image file to a Base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")