# AutoGen Studio Model Cards

## Powerful AI Models for Seamless Integration in AutoGen Studio

AutoGen Studio offers a suite of advanced AI models that can be easily integrated into your projects, enabling you to harness the power of cutting-edge language models, image generation capabilities, and multimodal functionalities. This README provides an overview of the available models and their key features.

### GPT-4

GPT-4 is a state-of-the-art language model that excels in natural language understanding and generation. With its advanced reasoning capabilities and contextual awareness, GPT-4 can handle complex queries, generate insightful responses, and assist in a wide range of language-related tasks.

### Model Card: GPT-4

#### Deployment Information

- **Deployment Name**: gpt-4
- **Model Name**: gpt-4
- **Type**: azure
- **Model Version**: 0125-Preview
- **Release Date**: 2024-02-15 (Preview Version)
- **Version Update Policy**: Updated once a new default version is available.

#### Deployment Specifications

- **Deployment Type**: Standard
- **Content Filter**: Default
- **Tokens per Minute Rate Limit**: 70,000 tokens
- **Requests per Minute Rate Limit**: 420 requests
- **Location**: Azure OpenAI Deployed Model (east) region

### Orca-2-13B

Orca-2-13B is an open-source language model known for its exceptional reasoning abilities. It can tackle intricate queries, provide in-depth analysis, and generate meaningful insights. Being open-source, Orca-2-13B offers flexibility in deployment, allowing for both local and cloud-based integration.

### Model Card: Orca-2-13B

#### Deployment Information

- **Deployment Name**: orca-2-13b
- **Model Name**: Orca-2-13B-GGUF
- **Type**: Opensource
- **Model Version**: 13 billion parameters
- **Release Date**: 2023-10-01
- **Version Update Policy**: Updated annually or as significant improvements are made.

#### Deployment Specifications

- **Deployment Type**: Hybrid (Local and Cloud)
- **Content Filter**: N/A
- **Tokens per Minute Rate Limit**: N/A (not token-based)
- **Requests per Minute Rate Limit**: Depends on deployment configuration
- **Location**: Can be deployed locally or on Azure as part of an integrated AI solution

#### Key Features and Use Cases

- **Reasoning Capabilities**: Known for its advanced reasoning capabilities, Orca2 can handle complex queries and generate insights, making it particularly useful for projects that require in-depth analysis and interpretation.
- **Flexibility in Deployment**: Being open-source, Orca2 allows for a flexible deployment strategy. It can be run entirely locally or integrated into cloud-based services depending on the needs of the project.
- **Integration with AutoGen Studio**: Orca2 is fully compatible with AutoGen Studio, allowing it to benefit from AutoGen’s low-code platform capabilities, which facilitate the development of AI solutions using natural language commands.

#### Usage Example

Here’s a Python code example that demonstrates a typical setup for using Orca2 within a local development environment:

```python
import requests

# Base URL for the Orca-2-13B model running locally
base_url = 'http://localhost:1234/v1'

# Sample query to the Orca2 model
response = requests.post(
    f"{base_url}/query",
    json={"query": "Explain the reasoning behind the stock market fluctuations today."}
)

# Extracting the response
data = response.json()
print(data['answer'])
```

### DALL-E 3

DALL-E 3 is a powerful image generation model that creates high-quality, creative visuals from textual descriptions. With support for high-resolution images and customizable output, DALL-E 3 enables the creation of unique and tailored visual content for various creative needs.

### Model Card: DALL-E 3

#### Deployment Information

- **Deployment Name**: dalle-3
- **Model Name**: dalle-3
- **Type**: azure
- **Model Version**: 1.0
- **Release Date**: 2024-03-01
- **Version Update Policy**: Updated once a new default version is available.

#### Deployment Specifications

- **Deployment Type**: Standard
- **Content Filter**: Default
- **Tokens per Minute Rate Limit**: N/A (not token-based)
- **Requests per Minute Rate Limit**: 100 requests
- **Location**: Azure OpenAI Deployed Model (east) region

#### Key Features and Use Cases

- **Image Generation Capabilities**: DALL-E 3 excels in generating high-quality, creative images from textual descriptions, providing unique visual content that can be tailored to a wide range of creative needs.
- **High Resolution**: Supports creation of images up to 1024x1024 pixels, enabling detailed and clear visuals.
- **Customizable Output**: Offers parameters for adjusting the style and elements of the generated images, catering to specific aesthetic requirements or thematic demands.

#### Usage Example

The following Python code example demonstrates how to generate an image with DALL-E 3 using the Azure OpenAI API:

```python
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-03-01",
    azure_endpoint="https://xeekai.openai.azure.com/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="<the user's prompt>",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
```

#### Note

When integrating or deploying models within your workflows or agents, it's essential to ensure their configurations align with your project's requirements and constraints. After creating or editing your model configurations, remember to update your workflows to reflect these changes for consistent and accurate performance.

This model card for DALL-E 3 aligns with the structure and detail of the other model cards, providing clear information about deployment, features, and usage.

### GPT-4 Turbo with Vision

GPT-4 Turbo with Vision combines the language understanding capabilities of GPT-4 Turbo with the ability to interpret and generate descriptions from images. This multimodal functionality makes it ideal for applications requiring visual data interpretation alongside textual data processing, such as educational tools, content creation, and customer support systems.

### Model Card: GPT-4 Turbo with Vision

#### Deployment Information

- **Deployment Name**: gpt-4-turbo-vision
- **Model Name**: GPT-4 Turbo with Vision
- **Type**: azure
- **Model Version**: 2024-12-01-preview
- **Release Date**: 2024-04-01
- **Version Update Policy**: Updated as new features or improvements are available.

#### Deployment Specifications

- **Deployment Type**: Standard
- **Content Filter**: Default
- **Tokens per Minute Rate Limit**: N/A (not token-based)
- **Requests per Minute Rate Limit**: 60 requests
- **Location**: Azure OpenAI Deployed Model (east) region

#### Key Features and Use Cases

- **Vision Capabilities**: Combines the powerful language understanding of GPT-4 Turbo with the ability to interpret and generate descriptions from images, enhancing multimodal applications.
- **Multimodal Functionality**: Capable of handling both text and image inputs simultaneously, providing a more holistic approach to data analysis and interaction.
- **Enhanced Interaction**: Ideal for applications requiring visual data interpretation alongside textual data processing, such as educational tools, content creation, and customer support systems.

#### Usage Example

Here’s a basic example of how you might use the GPT-4 Turbo with Vision model with code:

```python
import requests
import base64

# Define your Azure OpenAI resource endpoint and key.
RESOURCE_NAME = 'your_resource_name'
DEPLOYMENT_NAME = 'your_deployment_name'
API_KEY = 'your_api_key'

# Encode a local image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = 'path_to_your_local_image.jpg'
base64_image = encode_image_to_base64(image_path)

# Sample request body for the Chat Completion API with image data
request_body = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": [{"type": "text", "text": "Describe this picture:"},
                                     {"type": "image_url", "image_url": {"url": base64_image}}]},
    ],
    "max_tokens": 100,
    "stream": false
}

# Make the API call
response = requests.post(
    f'https://{RESOURCE_NAME}.openai.azure.com/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2023-12-01-preview',
    headers={'Content-Type': 'application/json', 'api-key': API_KEY},
    json=request_body
)

# Print the response
print(response.json())
```

Remember to replace the placeholders with your actual Azure OpenAI resource details and local image path.

#### Note

Integration of GPT-4 Turbo with Vision into your workflows or systems should align with your operational needs and security requirements. This model enables powerful multimodal interactions, which can enhance user experience and operational efficiency. Regular updates and calibration may be required to maintain performance and adapt to evolving use cases.

### Claude Opus

Claude Opus is an advanced language model designed for handling complex and nuanced conversations. With its customizable responses and high scalability, Claude Opus is well-suited for enterprise applications requiring deep contextual understanding and reliable performance under high demand.

### Model Card: Claude Opus

#### Deployment Information

- **Deployment Name**: claude-3-opus
- **Model Name**: Claude-3 Opus-20240229
- **Type**: anthropic
- **Model Version**: 20240229
- **Release Date**: 2024-02-29
- **Version Update Policy**: Updated semi-annually or as significant improvements are made.

#### Deployment Specifications

- **Deployment Type**: API-based
- **Content Filter**: Advanced AI-based moderation in place
- **Tokens per Minute Rate Limit**: Depends on the subscription plan
- **Requests per Minute Rate Limit**: Customizable based on user requirements
- **Location**: Hosted on Anthropic's secure cloud servers

#### Key Features and Use Cases

- **Advanced Natural Language Understanding**: Claude Opus is designed to handle complex and nuanced conversations, making it ideal for applications requiring deep contextual understanding.
- **Customizable Responses**: Offers flexibility in generating responses based on user preferences, which can be tailored for different domains like customer service, content generation, and more.
- **High Scalability**: Supports large-scale deployments for enterprise applications, ensuring reliable performance under high demand.

#### Usage Example

Here’s a Python code example demonstrating how to send a request to the Claude Opus model to create a message with specific parameters:

```python
import anthropic

# Initialize the Anthropic API client
client = anthropic.Anthropic(api_key="my_api_key")

# Create a message using the Claude-3 Opus model
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=4000,
    temperature=0,
    system="""\
    Microsoft AutoGen Group Chat Setup with PowerBI Report Vision Analyzer Workflow

    You are an expert on creating Microsoft AutoGen code for a given input. You will create code for the different agents required for the complex task of implementing a sophisticated workflow that automates the process of exporting Power BI reports as images, reviewing these images for design quality and clarity, and making design recommendations based on industry standards and GPT-4 Vision insights. This involves setting up a simulated group chat environment using Microsoft AutoGen's agent framework to manage and coordinate the interactions between specialized agents equipped with specific skills relevant to each step of the workflow.

    For more details and examples, refer to the accompanying documentation and usage guide on the specific implementation of the PowerBI Report Vision Analyzer workflow.
    """
)

# Print the generated content from the message
print(message.content)
```

#### Note

When integrating Claude Opus into your applications or workflows, ensure that the configuration aligns with your project's needs, particularly in terms of data security, response accuracy, and throughput requirements. Regular updates and maintenance are recommended to leverage the latest improvements and maintain optimal performance.

### GPT-4 Vision

GPT-4 Vision is a cutting-edge model that combines advanced visual and textual interpretation capabilities. It can understand and respond to queries related to visual content, perform optical character recognition (OCR) and object detection, and provide detailed descriptions, contextual insights, and actionable recommendations based on images.

### Model Card: GPT-4 Vision

#### Deployment Information

- **Deployment Name**: gpt-4-vision
- **Model Name**: GPT-4 Vision
- **Type**: OpenAI
- **Model Version**: gpt-4-turbo-2024-04-09
- **Release Date**: 2024-04-09
- **Version Update Policy**: Regular updates to incorporate advancements in AI vision technology and user feedback.

#### Deployment Specifications

- **Deployment Type**: Cloud-based API
- **Content Filter**: Advanced content filtering capabilities to ensure the appropriateness of visual and textual outputs.
- **Tokens per Minute Rate Limit**: Configurable based on the user's subscription plan and usage.
- **Requests per Minute Rate Limit**: Configurable to accommodate high-demand scenarios.
- **Location**: Hosted on OpenAI's servers, available globally with data residency considerations.

#### Key Features and Use Cases

- **Advanced Visual and Textual Interpretation**: Employs cutting-edge AI to interpret complex images and text, providing detailed descriptions, contextual insights, and actionable recommendations.
- **Visual Question Answering (VQA)**: Capable of understanding and responding to queries directly related to visual content, which is crucial for applications like dashboard analysis, medical imaging, and retail.
- **Optical Character Recognition (OCR) and Object Detection**: Enhances the ability to detect and interpret textual and object details within images, supporting use cases in document processing, automated inventory management, and navigation systems.

#### Application in Specific Domains

- **Marketing and Content Creation**: Generates compelling visual content descriptions and suggestions, enhancing engagement through targeted marketing strategies and creative processes.
- **Technical and Engineering Fields**: Analyzes diagrams, blueprints, and technical drawings to provide explanations, operational details, or troubleshooting steps.

#### Enhanced Features

- **JSON Mode and Reproducible Outputs**: Offers structured output modes and reproducibility for consistent application results, essential for integration into business intelligence tools like Power BI.
- **Rate Limits and Cost Management**: Provides customizable options to manage operational costs effectively while maintaining high performance and response accuracy.

#### Usage Example

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo-2024-04-09",
  messages=[
    {
      "role": "system",
      "content": "Assist in optimizing this Power BI dashboard based on the visual data provided."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "<base64_encoded_image>"
          }
        },
        {
          "type": "text",
          "text": "Provide detailed recommendations for dashboard optimization."
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Output the response
print(response['choices'][0]['message']['content'])
```

#### Note

When integrating GPT-4 Vision into your workflows or applications, consider operational needs such as data privacy, response latency, and throughput. Regular reviews and updates are recommended to harness new features effectively and ensure compliance with data protection regulations. Adjust configurations based on evolving user requirements and technological advancements to optimize performance and user experience.

## Getting Started

To start using these models in your AutoGen Studio projects, refer to the individual model cards for detailed information on deployment specifications, key features, and usage examples. Each model card provides code snippets and guidelines to help you integrate the models seamlessly into your workflows.

## Best Practices

When working with these models, consider the following best practices:

- Align model configurations with your project's requirements and constraints.
- Update your workflows to reflect any changes made to model configurations.
- Ensure data privacy and security when integrating models into your applications.
- Regularly review and update models to leverage new features and improvements.
- Adjust configurations based on evolving user requirements and technological advancements.

## Support and Resources

For further assistance and resources, refer to the AutoGen Studio documentation and community forums. Our team is dedicated to providing the support you need to make the most of these powerful AI models in your projects.
