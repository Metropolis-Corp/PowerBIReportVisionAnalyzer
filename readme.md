# AutoGen Studio: Power BI Report Vision Analyzer

AutoGen Studio is a powerful platform that enables the creation of sophisticated AI-driven workflows using natural language commands. This repository showcases the implementation of the Power BI Report Vision Analyzer workflow, which automates the process of exporting Power BI reports as images, reviewing these images for design quality and clarity, and making design recommendations based on industry standards and GPT-4 Vision insights.

Continue the conversation with on ChatGPT with "PowerBI Report Vision Analyzer" <https://chat.openai.com/g/g-aoqysiABA-powerbi-report-vision-analyzer>

## Table of Contents

- [AutoGen Studio: Power BI Report Vision Analyzer](#autogen-studio-power-bi-report-vision-analyzer)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Key Features](#key-features)
  - [Getting Started](#getting-started)
  - [Workflow](#workflow)
  - [Agents](#agents)
  - [Skills](#skills)
  - [Models](#models)
  - [Configuration](#configuration)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The Power BI Report Vision Analyzer workflow leverages the capabilities of AutoGen Studio to streamline the process of analyzing and optimizing Power BI reports. By combining advanced AI models, such as GPT-4 Vision, with specialized agents and skills, this workflow provides actionable recommendations to enhance the design, clarity, and impact of Power BI reports.

## Key Features

- Automated export of Power BI report pages as images
- Deep insights extraction from exported images using GPT-4 Vision
- Dynamic design criteria and benchmarks for superior visual quality
- Interactive visualization of proposed changes and recommendations
- Performance optimizations and error handling mechanisms
- Compliance with data protection regulations (e.g., GDPR)

## Getting Started

To get started with the Power BI Report Vision Analyzer workflow, follow these steps:

1. Clone this repository: `git clone https://github.com/Metropolis-Corp/gpt4vision.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the necessary API keys and credentials in the `config.py` file
4. Review the agents, skills, and workflows to understand their functionalities
5. Run the main script to initiate the workflow: `python main.py`

For detailed instructions and examples, please refer to the [documentation](docs/README.md).

## Workflow

The Power BI Report Vision Analyzer workflow consists of the following steps:

1. **ExportToImage**: Exports a Power BI report page as an image using optimized Power BI REST APIs or scripting capabilities.
2. **AnalyzeImageWithGPT4Vision**: Utilizes Azure OpenAI GPT-4 Vision API to extract deep insights from the exported images, focusing on design quality and content clarity.
3. **ImageQualityReview**: Reviews the image against dynamically updated design criteria and benchmarks for superior visual quality and clarity.
4. **DesignRecommendations**: Generates and dynamically refines design recommendations, providing interactive visualization for proposed changes.

For more details on the workflow, refer to the [Workflow_PowerBIReportVisionAnalyzer.json](workflows/Workflow_PowerBIReportVisionAnalyzer.json) file.

## Agents

The Power BI Report Vision Analyzer workflow utilizes the following agents:

- **Coder**: Handles API interactions and processes image-related tasks efficiently.
- **Product Manager**: Provides creative ideas and insights for software product development.
- **User Proxy**: Handles all administrative commands and user verifications.

For more information on each agent, refer to the respective agent files in the [agents](agents/) directory.

## Skills

The workflow incorporates various skills to accomplish specific tasks:

- **AdvancedDAXOptimization**: Optimizes DAX queries for improved performance and efficiency.
- **AnalyzeImageWithGPT4Vision**: Analyzes images using GPT-4 Vision to extract insights, summaries, or specific data points.
- **AuthenticateWithPowerBI**: Authenticates with the Power BI service using secure credentials.
- **EncodeImageForAnalysis**: Encodes images in a suitable format for analysis by GPT-4 Vision.
- **ExportToImage**: Exports Power BI report pages as high-quality images.
- **GenerateDesignRecommendations**: Generates actionable design recommendations based on industry standards and best practices.
- **PowerBIFieldInterpreter**: Interprets and explains the meaning and usage of fields in a Power BI dataset.

For more details on each skill, refer to the respective skill files in the [skills](skills/) directory.

## Models

The Power BI Report Vision Analyzer workflow leverages advanced AI models, such as GPT-4 and GPT-4 Vision, to enable intelligent analysis and recommendations. The model card in the [models](models/) directory provides information about the deployed models, including their capabilities, limitations, and usage guidelines.

## Configuration

The `config.py` file contains the necessary configuration settings for the Power BI Report Vision Analyzer workflow. Make sure to update the file with your specific API keys, credentials, and other relevant settings before running the workflow.

## Contributing

Contributions to the Power BI Report Vision Analyzer workflow are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. For major changes, please discuss them with the project maintainers first.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---

We hope you find the Power BI Report Vision Analyzer workflow useful and valuable in enhancing your Power BI reports. If you have any questions or need further assistance, please don't hesitate to reach out to our support team.

Happy analyzing and optimizing your Power BI reports with AutoGen Studio!
