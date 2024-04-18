"""
This module provides the EncodeImageForAnalysis skill for encoding images.
"""

import base64
import os
from autogen import Skill, SkillExecutionError, logger


class EncodeImageForAnalysis(Skill):
    """
    Encodes the exported report image in a format (e.g., base64) that is
    compatible with GPT-4 Vision API requests, ensuring the image file exists,
    is within size limits, and logs the encoding process for troubleshooting.
    """

    name = "EncodeImageForAnalysis"
    description = "Encodes the exported report image for analysis."

    input_schema = {
        "type": "object",
        "properties": {
            "image_file": {
                "type": "string",
                "description": "The path of the image file to be encoded."
            }
        },
        "required": ["image_file"]
    }

    output_schema = {
        "type": "object",
        "properties": {
            "encoded_image": {
                "type": "string",
                "description": "The string representation of the encoded image."
            }
        },
        "required": ["encoded_image"]
    }

    def execute(self, input_data):
        self.validate_input(input_data)

        image_file = input_data["image_file"]

        # Validate file extension (simple check for demonstration)
        if not image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise SkillExecutionError(
                "Image file is not in an expected format (.png, .jpg, .jpeg)"
            )

        # Validate and encode the image file
        encoded_image = self.encode_image(image_file)

        output_data = {"encoded_image": encoded_image}
        self.validate_output(output_data)
        return output_data

    def encode_image(self, image_path):
        # Validate the image file path
        if not os.path.exists(image_path):
            raise SkillExecutionError(f"Image file not found: {image_path}")

        # Check file size (example limit: 5 MB)
        MAX_IMAGE_SIZE_MB = 5
        file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
        if file_size_mb > MAX_IMAGE_SIZE_MB:
            raise SkillExecutionError(
                f"Image file exceeds the maximum size of {MAX_IMAGE_SIZE_MB} MB: "
                f"{image_path}"
            )

        # Log the encoding process
        logger.info(f"Encoding image: {image_path}, size: {file_size_mb:.2f} MB")

        try:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                return encoded_image
        except Exception as e:
            logger.error(f"Failed to encode image: {e}")
            raise SkillExecutionError(f"Failed to encode image: {str(e)}") from e