import os
import json
import logging
from azure.identity import DefaultAzureCredential
from azure.ai.openai import ConversationClient
from autogen.exceptions import SkillExecutionError
import autogen
from config import AZURE_OPENAI_ENDPOINT  # Import the endpoint

class GenerateDesignRecommendations(autogen.Skill):
    """
    Generates and iteratively refines design recommendations for the Power BI report image, utilizing insights from GPT-4 Vision.

    Attributes:
        azure_credential (DefaultAzureCredential): Azure credential object for authentication.
        client (ConversationClient): Client for interacting with the Azure OpenAI API.
    """

    name = "GenerateDesignRecommendations"
    description = "Utilizes insights from GPT-4 Vision to generate design recommendations for Power BI reports."

    input_schema = {
        "type": "object",
        "properties": {
            "insights": {
                "type": "string",
                "description": "Insights from GPT-4 Vision analysis to be used for generating design recommendations."
            }
        },
        "required": ["insights"]
    }

    output_schema = {
        "type": "object",
        "properties": {
            "recommendations": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "A list of design improvements and best practice tips based on the insights provided."
            }
        },
        "required": ["recommendations"]
    }

    def __init__(self):
        super().__init__()
        self.azure_credential = DefaultAzureCredential()
        endpoint = AZURE_OPENAI_ENDPOINT  # Use the imported endpoint
        if not endpoint:
            raise ValueError("Azure OpenAI endpoint is not configured.")
        self.client = ConversationClient(endpoint=endpoint, credential=self.azure_credential)
        logging.basicConfig(level=logging.INFO)

    def execute(self, input_data):
        """
        Executes the skill to generate design recommendations based on GPT-4 Vision insights.

        Args:
            input_data (dict): Input data containing insights.

        Returns:
            dict: Output data containing a list of recommendations.
        """
        self.validate_input(input_data)

        insights = input_data["insights"]
        recommendations = self.get_design_recommendations(insights)

        output_data = {"recommendations": recommendations}
        self.validate_output(output_data)
        return output_data

    def get_design_recommendations(self, insights):
        """
        Queries the GPT-4 model to generate design recommendations based on provided insights.

        Args:
            insights (str): Insights from GPT-4 Vision.

        Returns:
            list: Design recommendations as a list of strings.
        """
        prompt_text = f"Based on the following insights: {insights}, provide design recommendations to enhance the clarity and visual appeal of the Power BI report."
        try:
            response = self.client.create_completion(
                model="gpt-4",
                prompt=prompt_text,
                max_tokens=250
            )
            if response.choices and response.choices[0].text:
                return response.choices[0].text.strip().split("\n")
            else:
                logging.error("No recommendations received or unexpected response format.")
                raise SkillExecutionError("Unexpected response format or no recommendations from API.")
        except Exception as e:
            logging.error(f"API error: {str(e)}")
            raise SkillExecutionError(f"API error: {str(e)}")

    def validate_input(self, input_data):
        """
        Validates the input data against the defined input schema.

        Args:
            input_data (dict): Input data to validate.
        
        Raises:
            SkillExecutionError: If the input data is invalid.
        """
        # This is a placeholder for actual schema validation code
        if "insights" not in input_data:
            logging.error("Invalid input: Missing required insights")
            raise SkillExecutionError("Invalid input: Missing required insights")

    def validate_output(self, output_data):
        """
        Validates the output data against the defined output schema.

        Args:
            output_data (dict): Output data to validate.
        
        Raises:
            SkillExecutionError: If the output data is invalid.
        """
        # This is a placeholder for actual schema validation code
        if "recommendations" not in output_data:
            logging.error("Invalid output: Missing required recommendations")
            raise SkillExecutionError("Invalid output: Missing required recommendations")

# Example usage
if __name__ == "__main__":
    skill_instance = GenerateDesignRecommendations()
    input_example = {"insights": "Here are detailed insights about your Power BI report's design."}
    try:
        result = skill_instance.execute(input_example)
        print(result)
    except SkillExecutionError as e:
        logging.error(f"Error executing skill: {str(e)}")
