"""
Microsoft AutoGen Group Chat Setup with PowerBI Report Vision Analyzer Workflow

You are an expert on creating Microsoft AutoGen code for a given input. You will create code for the different agents required for the complex task of implementing a sophisticated workflow that automates the process of exporting Power BI reports as images, reviewing these images for design quality and clarity, and making design recommendations based on industry standards and GPT-4 Vision insights. This involves setting up a simulated group chat environment using Microsoft AutoGen's agent framework to manage and coordinate the interactions between specialized agents equipped with specific skills relevant to each step of the workflow.

(find many examples of AutoGen implementation here: "https://github.com/microsoft/autogen/tree/main/notebook" and "https://raw.githubusercontent.com/microsoft/autogen/main/notebook/agentchat_microsoft_fabric.ipynb") 

Configuration:
- `llm_config`: Dictionary containing the configuration for the language learning model (LLM) with GPT-4 parameters, ensuring consistency and reliability.
  - `config_list`: Specific settings for GPT-4.
  - `cache_seed`: Fixed seed value (42) for deterministic behavior in caching mechanisms.
  - `timeout_seconds`: Maximum time allowed for each agent's response (default: 30 seconds).
  - `error_handling`: Specifies how to handle errors during agent interactions (default: "graceful").

Agents:
1. User Proxy Agent (`user_proxy`):
   - Acts as a human administrator within the chat, orchestrating the workflow and managing user inputs.
   - Adheres to the operational context of the workflow by considering the last 2 messages and operating within the "groupchat" directory.
   - Human input mode set to "INTERACTIVE" for dynamic interactions with users.

2. Coder Agent (`coder`):
   - Handles code-related queries or operations related to exporting images and interacting with Power BI and Azure OpenAI APIs.
   - Shares the same LLM configuration as other agents to maintain uniformity in processing.
   - Adapts capabilities dynamically as workflow requirements evolve.

3. Product Manager Agent (`pm`):
   - Focuses on providing insights and suggestions that drive the visual and design recommendations for Power BI reports.
   - Engages creatively to synthesize insights from image analyses and formulate improvement strategies.
   - Employs the same LLM configuration to ensure seamless integration with other agents.

Workflow Execution:
- The workflow is meticulously defined to include agents that perform tasks ranging from exporting images to generating design recommendations.
- Each agent in the workflow has specific tasks and optimizations that ensure efficient and reliable execution of their respective roles.

Group Chat Manager:
- Coordinates the interactions between agents, managing data flow and ensuring that all steps in the workflow are executed as planned.

Interface:
- A user-friendly interface (`GroupChatInterface`) is provided to allow users to interact seamlessly with the automated workflow.
- Offers capabilities for starting and managing chat sessions that facilitate the entire report visualization enhancement process.

For more details and examples, refer to the accompanying documentation and usage guide on the specific implementation of the PowerBI Report Vision Analyzer workflow.
"""

import autogen

# Configuration for the language learning model with specific GPT-4 parameters and a fixed seed for consistency
llm_config = {
    "config_list": config_list_gpt4,
    "cache_seed": 42,
    "timeout_seconds": 30,
    "error_handling": "graceful"
}

# User Proxy Agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="Facilitates administrative commands and user interactions, directing workflow operations.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="INTERACTIVE",
    error_policy="log_and_continue"
)

# Coder Agent
coder = autogen.AssistantAgent(
    name="Coder",
    system_message="Assists with code-related tasks for API interactions and data handling.",
    llm_config=llm_config,
    error_policy="log_and_continue"
)

# Product Manager Agent
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Delivers creative product insights and recommendations for report design improvements.",
    llm_config=llm_config,
    error_policy="log_and_continue"  
)

# Group Chat Setup
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)

# Group Chat Manager
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Interface for Agent Interaction
groupchat_interface = autogen.GroupChatInterface(manager)
groupchat_interface.start_session()