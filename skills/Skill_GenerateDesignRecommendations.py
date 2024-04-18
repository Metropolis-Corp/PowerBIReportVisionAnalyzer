import os
import logging
from azure.identity import DefaultAzureCredential
from openai.azure_openai import AzureOpenAI  # Ensure this import matches the actual library structure
import autogen
from config import AZURE_OPENAI_ENDPOINT
from autogen.exceptions import SkillExecutionError

# Configure logging at the script level to avoid reconfiguration inside classes
logging.basicConfig(level=logging.INFO)

class GenerateDesignRecommendations(autogen.Skill):
    name = "GenerateDesignRecommendations"
    description = "Utilizes insights from GPT model to generate design recommendations for Power BI reports."

    input_schema = {
        "type": "object",
        "properties": {
            "insights": {"type": "string", "description": "Insights to be used for generating design recommendations."}
        },
        "required": ["insights"]
    }

    output_schema = {
        "type": "object",
        "properties": {
            "recommendations": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of design improvements based on the insights provided."
            }
        },
        "required": ["recommendations"]
    }

    def __init__(self):
        super().__init__()
        self.azure_credential = DefaultAzureCredential()
        self.client = AzureOpenAI(api_key=os.getenv("AZURE_OPENAI_API_KEY"), azure_endpoint=AZURE_OPENAI_ENDPOINT, api_version="2024-02-01")

    def execute(self, input_data):
        self.validate_input(input_data)
        insights = input_data["insights"]
        recommendations = self.get_design_recommendations(insights)
        output_data = {"recommendations": recommendations}
        self.validate_output(output_data)
        return output_data

    def get_design_recommendations(self, insights):
        prompt_text = f"Based on the following insights: {insights}, provide design recommendations."
        try:
            response = self.client.completions.create(model="your-deployment-name", prompt=prompt_text, max_tokens=250)
            if response.choices and response.choices[0].text:
                return response.choices[0].text.strip().split("\n")
            else:
                logging.error("No recommendations received or unexpected response format.")
                raise SkillExecutionError("Unexpected response format or no recommendations from API.")
        except Exception as e:
            logging.error(f"API error: {str(e)}")
            raise SkillExecutionError(f"API error: {str(e)}")

    # validate_input and validate_output methods remain unchanged

# Example usage
if __name__ == "__main__":
    skill_instance = GenerateDesignRecommendations()
    input_example = {"insights": "Here are detailed insights about your Power BI report's design."}
    try:
        result = skill_instance.execute(input_example)
        print(result)
    except SkillExecutionError as e:
        logging.error(f"Error executing skill: {str(e)}")
