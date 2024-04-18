import os
import base64
import json
import mimetypes
import imghdr
from openai import AzureOpenAI
from openai.error import APIError, APIConnectionError, RateLimitError, AuthenticationError
from autogen.skill_base import Skill, SkillExecutionError
from jsonschema import validate, ValidationError

# Initialize the Azure OpenAI client with necessary API details
client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://xeekai.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)


class AnalyzeImageWithGPT4Vision(Skill):
    name = "AnalyzeImageWithGPT4Vision"
    description = "Analyzes images using GPT-4 Vision to extract insights, summaries, or specific data points."

    # Define input and output JSON schema for validation
    input_schema = {
        "type": "object",
        "properties": {
            "image_file": {
                "type": "string",
                "description": "Path to the image file to be analyzed."
            },
            "question": {
                "type": "string",
                "description": "Question to pose regarding the image."
            }
        },
        "required": ["image_file", "question"]
    }

    output_schema = {
        "type": "object",
        "properties": {
            "answer": {
                "type": "string",
                "description": "Answer generated by GPT-4 Vision based on the image and question."
            }
        },
        "required": ["answer"]
    }

    def execute(self, input_data):
        self.validate_input(input_data)
        image_file = input_data["image_file"]
        question = input_data["question"]

        if not os.path.isfile(image_file):
            raise SkillExecutionError(
                f"Image file does not exist: {image_file}")

        # Check if the file is a supported image format
        file_type, _ = mimetypes.guess_type(image_file)
        if file_type not in ["image/png", "image/jpeg", "image/jpg"]:
            raise SkillExecutionError(
                f"Unsupported image format. Supported formats: PNG, JPEG, JPG.")

        # Further validate the image content
        detected_format = imghdr.what(image_file)
        if detected_format not in ["png", "jpeg", "jpg"]:
            raise SkillExecutionError(
                f"Image content does not match the expected format.")

        image_data = self.encode_image(image_file)
        answer = self.ask_gpt4_vision(image_data, question)
        output_data = {"answer": answer}
        self.validate_output(output_data)
        return output_data

    def encode_image(self, image_path):
        """
        Encode the image file in base64 format.
        :param image_path: Path to the image file.
        :return: Base64 encoded image data.
        """
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            raise SkillExecutionError(f"File not found: {image_path}")

    def ask_gpt4_vision(self, image_data, question, max_tokens=250, temperature=0.5):
        """
        Submit the base64-encoded image and question to the GPT-4 Vision API and retrieve the answer.
        :param image_data: Base64 encoded image data.
        :param question: Question to pose regarding the image.
        :param max_tokens: Maximum number of tokens in the generated answer.
        :param temperature: Sampling temperature for generating the answer.
        :return: Generated answer from GPT-4 Vision.
        """
        try:
            response = client.Completion.create(
                model="gpt-4-vision",
                prompt=question,
                attachments=[{
                    "data": f"data:image/png;base64,{image_data}",
                    "type": "image/png"
                }],
                max_tokens=max_tokens,
                temperature=temperature
            )
            if response.choices and response.choices[0].text:
                return response.choices[0].text.strip()
            else:
                raise SkillExecutionError(
                    "Unexpected response format from GPT-4 Vision API.")
        except RateLimitError as e:
            raise SkillExecutionError(f"Rate limit exceeded: {str(e)}")
        except AuthenticationError as e:
            raise SkillExecutionError(f"Authentication error: {str(e)}")
        except APIError as e:
            raise SkillExecutionError(f"API error: {str(e)}")
        except APIConnectionError as e:
            raise SkillExecutionError(f"API connection error: {str(e)}")
        except Exception as e:
            raise SkillExecutionError(f"Unexpected error: {str(e)}")

    def validate_input(self, input_data):
        """
        Validates the input data against the defined input schema.
        :param input_data: Input data to validate.
        :raises SkillExecutionError: If the input data is invalid.
        """
        try:
            validate(instance=input_data, schema=self.input_schema)
        except ValidationError as e:
            raise SkillExecutionError(f"Invalid input data: {str(e)}")

    def validate_output(self, output_data):
        """
        Validates the output data against the defined output schema.
        :param output_data: Output data to validate.
        :raises SkillExecutionError: If the output data is invalid.
        """
        try:
            validate(output_data, self.output_schema)
        except ValidationError as e:
            raise SkillExecutionError(f"Invalid output data: {str(e)}")


# Ensure the module can be easily executed or tested
if __name__ == "__main__":
    skill_instance = AnalyzeImageWithGPT4Vision()
    input_example = {"image_file": "path/to/image.png",
                     "question": "What does this image depict?"}
    try:
        result = skill_instance.execute(input_example)
        print(result)
    except SkillExecutionError as e:
        print(f"Error executing skill: {str(e)}")
