import os
import base64
from PIL import Image
import io
import logging

class LoadImageForChat:
    """
    A skill to load an image from the 'sandbox' directory and prepare it for chat interactions.
    """
    def __init__(self, image_path='./sandbox/image.png'):
        """
        Initializes the skill with the path to the image.
        
        Args:
            image_path (str): The path to the image file.
        """
        self.image_path = image_path
        self.image_data = None
        self.base64_image = None

    def load_image(self):
        """
        Loads the image from the specified path and encodes it to Base64.
        
        Raises:
            FileNotFoundError: If the image file does not exist.
            Exception: For other issues that might occur during file handling.
        """
        try:
            with Image.open(self.image_path) as img:
                buffered = io.BytesIO()
                img.save(buffered, format=img.format)
                self.image_data = buffered.getvalue()
                self.base64_image = base64.b64encode(self.image_data).decode('utf-8')
        except FileNotFoundError as e:
            logging.error(f"The image file was not found: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the image: {e}")
            raise

    def get_base64_image(self):
        """
        Returns the Base64-encoded string of the image, suitable for embedding in HTML or JSON.

        Returns:
            str: Base64-encoded image data.
        """
        if self.base64_image is None:
            self.load_image()
        return self.base64_image

# Example usage
if __name__ == "__main__":
    print(f"Current Working Directory: {os.getcwd()}")  # Print the current working directory
    image_loader = LoadImageForChat()
    try:
        base64_image = image_loader.get_base64_image()
        print(f"Base64 Image Data: {base64_image}")
    except Exception as e:
        logging.error(f"Failed to load and convert image: {e}")
