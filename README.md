# Personalized Learning Path Curator Crew

## Description

This CrewAI-powered application acts as a **Personalized Learning Path Curator**. It addresses the common problem faced by individuals wanting to learn a new skill or topic online: being overwhelmed by the vast amount of available resources (courses, tutorials, articles, videos) and struggling to find a structured, relevant, and high-quality learning path.

This crew automates the process of:

1.  **Understanding User Needs:** Captures the desired learning topic and makes reasonable assumptions about the user's level, preferred style, time commitment, and budget.
2.  **Discovering Resources:** Uses the DuckDuckGo search tool to find relevant online learning materials across various platforms.
3.  **Evaluating & Filtering:** Assesses the discovered resources for quality, relevance, and suitability based on the user's needs.
4.  **Structuring the Path:** Organizes the vetted resources into a logical, step-by-step learning path with distinct modules.
5.  **Presenting the Plan:** Compiles the final path into a clean, easy-to-follow **Markdown** report.

**Value Proposition:**

*   **Saves Time:** Drastically reduces the hours users would spend manually searching and vetting resources.
*   **Reduces Overwhelm:** Provides a clear, actionable starting point instead of an endless list of options.
*   **Increases Effectiveness:** Creates structured paths likely leading to better learning outcomes compared to haphazard searching.
*   **Personalization:** Tailors recommendations based on the specific topic requested.
*   **Leverages AI:** Utilizes Google's Gemini model for intelligent analysis, structuring, and formatting, coordinated by the CrewAI framework.

## Example Use Cases

*   **Career Transition:** A graphic designer wants to learn **"User Experience (UX) Design Fundamentals"** to switch careers.
*   **Upskilling:** A software developer needs to get up to speed on **"Kubernetes for Developers"**.
*   **Academic Support:** A student looking for supplementary resources for **"Introduction to Organic Chemistry"**.
*   **Hobbyist Learning:** Someone wanting to learn **"Beginner's Guide to Digital Photography"** or **"How to Play the Ukulele"**.
*   **Staying Current:** A professional looking for resources on **"Latest Trends in Artificial Intelligence"**.

## Dependencies

To run this crew, you will need:

*   **Python:** Version 3.9 or higher recommended.
*   **CrewAI Libraries:**
    *   `crewai`
    *   `crewai_tools`
*   **Langchain Google Generative AI:**
    *   `langchain-google-genai`
    *   `google-generativeai` (usually installed as a dependency)
*   **Search Tool Library:**
    *   `duckduckgo-search`
*   **YAML Parser:**
    *   `ruamel.yaml` (used in `main.py` for loading YAML, can be replaced with `PyYAML` if preferred)
*   **Environment Variable Handler (Optional but Recommended):**
    *   `python-dotenv` (to load API keys from a `.env` file)
*   **API Keys:**
    *   **Google Generative AI API Key:** Obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Installation
While you can use uv or pip, it is recommended to let crewai do the job for you using the following  steps:
1. clone the project files from GitHub repository.
```bash
git clone https://github.com/farajallah/learning-path-creator
```
2. navigate to the crew
```bash
cd ./learning-path-creator/learning_path_creator_crew
```
3. crewai will create a virtual environment and insatll all dependencies for you.
```bash
crewai install
```
When the installation is done, most probably you will get an error, this is because you didn't configure the crew yet.
Please follow the instruction in the following section to do so.

## Configuration Instructions
 
1.  **Set model and API Key:**
    *   Create a file named `.env` in the project directory and add the required seetings:
        ```
        MODEL=\"MODEL_NAME_HERE\"
        GEMINI_API_KEY=\"YOUR_API_KEY_HERE\"
        ```
        The crew is gonfigured to use any model from gemini such as: gemini/gemini-2.0-flash, gemini/gemini-1.5-flash ...etc.  
        However, you can use any model form any other provider such as OpenAI. In this case you need to refer to their documentation in order to know how to configure the crew to use that model.  

2.  **Customize crew inputs and settings:**  
Input for the crew are found in `settings.yaml` file which is found in _```config```_ folder.  
In this file you will find the follwoing crew settings:
    1. verbose (true / false):  
    If true, the crew will provide detailed and extensive output or information while it is running. This is useful for debugging.

    2. tempreature (0.0 - 1.0):  
    This setting controls the creativity of the model's outputs. A value close to 0.0 means a more focused and deterministic model, while a value close to 1.0 means a more creative one.

    3. prompts:  
    To make the crew as customizable as possible, the following inputs are needed for the crew:
        - learning_topic: the topic you want to learn about.  
        e.g. python programming.
        - user_level: the current level of the user in that topic.  
        e.g. beginner.  
        - time_available: hours/week the user can dedicate to learn about the topic.  
        e.g. 3-5.    
        - max_cost: max amount (in $) the user can afford to pay for resources (courses, books).  
        e.g. 50.    
        - learning_goals: the goal that the user wants to achieve from learning this topic.  
        e.g. Obtain an overview of the topic.    
        - user_language: the language of the final report.  


3.  **Customize settings, agents and tasks (Optional):**  
    1.   **Agents:** Modify agent definitions in `agents.yaml`.  
    2.   **Tasks:** Adjust task descriptions, expected outputs in `tasks.yaml`.  

## Usage Example

1.  Navigate to the project directory in your terminal.
2.  Ensure your `GOOGLE_API_KEY` is configured.
3.  Run the crew:

    ```bash
    crewai run
    ```

4.  The script will prompt you for inputs one by one, enter your answer for each input and press [Enter]. 
For some questions a default value is set, if you are happy with this value just press [Enter].

    ```
    What topic do you want to learn about?
      Examples:
      - Learn Python Programming
      - Introduction to Quantum Computing
      Topic: <ENTER YOUR ANSWER HERE>

    What is your level in this topic?
    Examples: beginner, intermediate, advanced.
    Press [Enter] to use the default value (beginner): <ENTER YOUR ANSWER HERE>

    How many hours per week you internd to dedicate to learn this topic?
    Examples: 3, 5-7 ...etc.
    Press [Enter] to use the default value (3-5): <ENTER YOUR ANSWER HERE>

    What is the max cost in $ you internd to spend learning this topic?
    Examples: 50, 100, 300 ...etc.
    Press [Enter] to use the default value (50): <ENTER YOUR ANSWER HERE>

    What is your goal you intend to achieve by following the learnin plan?
    Examples: 
    - Gain foundational understanding and practical skills
    - Understand the basics of the topic
    - Obtain an overview of the topic
    Press [Enter] to use the default value (Obtain an overview of the topic)
    Goal: <ENTER YOUR ANSWER HERE>

    In what language you want the learning resouces to be?
    Examples:
    - Arabic
    - English
    - Turkish
    Press [Enter] to use the default value (English)
    Language: <ENTER YOUR ANSWER HERE>
    ```

5.  The crew will execute the tasks sequentially, showing verbose output if enabled. You will see agents thinking, using the DuckDuckGo tool, and passing information.

7.  **Expected Output:** After the crew finishes, it will save the final curated learning path in Markdown format to a file saved locally.  
An example of the expected output would be:

    ```markdown
    **Generated Learning Path (Markdown):**

    # Your Personalized Learning Path for Learn Rust Programming

    Here is a suggested path to get started with Learn Rust Programming, based on beginner-level assumptions and a mix of free/low-cost resources:

    ## Module 1: Foundational Concepts & Setup
    *   Focus: Grasp the absolute basics, installation, and 'Hello, World!'.
    *   Resource: [The Rust Programming Language Book (Official)](https://doc.rust-lang.org/book/) - Start here for the comprehensive, official guide. Read the initial chapters on installation and basic concepts.

    ## Module 2: Core Language Features
    *   Focus: Understand ownership, borrowing, structs, enums, and control flow.
    *   Resource: [The Rust Programming Language Book (Official)](https://doc.rust-lang.org/book/) - Continue through the core chapters.
    *   Resource: [Rustlings (Interactive Exercises)](https://github.com/rust-lang/rustlings) - Small exercises to get you coding and fix compiler errors. Excellent for practice.

    ## Module 3: Common Collections & Error Handling
    *   Focus: Learn about vectors, strings, hash maps, and Rust's approach to errors.
    *   Resource: [The Rust Programming Language Book (Official)](https://doc.rust-lang.org/book/) - Focus on chapters covering these topics.
    *   Resource: [Easy Rust (Simplified Explanations & Videos)](https://github.com/Dhghomon/easy_rust) - Offers alternative explanations and visual aids which can be helpful.
    ```
    *(Note: The exact resources and structure will vary based on the topic and the search results found at runtime.)*

    Good luck with your learning journey!
