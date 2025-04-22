# Personalized Learning Path Curator Crew

## 🚀 Overview

This crew automates the creation of personalized online learning paths for any specified topic, solving the common problem of resource overload and lack of structure when self-learning.

This crew enables users to receive a custom, step-by-step learning roadmap by leveraging a team of specialized AI agents (powered by Google Gemini) that collaborate to discover, evaluate, and organize relevant online resources.

## ✨ Key Features

- **Needs-Driven Curation**: Analyzes the requested learning topic and automatically sets reasonable assumptions for beginner level, common learning preferences, and budget constraints.
- **Targeted Resource Discovery**: Employs DuckDuckGo Search to find diverse online learning materials (courses, videos, articles, docs) relevant to the user's topic.
- **AI-Powered Evaluation & Filtering**: Assesses discovered resources for relevance, potential quality, and suitability based on the defined requirements, filtering down to the most promising options.
- **Structured Path Design**: Organizes the vetted resources into a logical, sequential learning path with clear modules using Markdown for readability.
- **Markdown Report Generation**: Presents the final, curated learning plan as a clean, actionable Markdown document.

## 🔍 Use Cases

This crew is ideal for:

- Individuals starting to learn a new programming language, framework, or technical skill (e.g., "Learn Python", "Introduction to React").
- Professionals looking to upskill or cross-skill in a specific domain (e.g., "Fundamentals of Digital Marketing", "Cloud Computing Basics").
- Students seeking supplementary learning resources for academic subjects (e.g., "Key Concepts in Microeconomics").
- Hobbyists wanting a structured approach to learning a new craft or skill (e.g., "Getting Started with 3D Printing").
- Anyone feeling overwhelmed by the sheer volume of online courses and tutorials who wants a clear starting point.

## 🛠️ Requirements

- **CrewAI version:** `0.28.8` or newer recommended.
- **API Keys needed:**
    - **Google Generative AI API Key**: Obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey). Must be set as the `GOOGLE_API_KEY` environment variable.
- **Additional Python dependencies:**
    - `langchain-google-genai`
    - `duckduckgo-search`
    - `ruamel.yaml` (or `PyYAML` if `main.py` is adjusted)
    - `python-dotenv` (recommended for managing API keys via `.env` file)

    Install using:
    ```bash
    pip install crewai crewai_tools langchain-google-genai google-generativeai duckduckgo-search python-dotenv ruamel.yaml
    ```

## 📊 Example Output

The crew produces a final report in **Markdown format**, delivered directly to the console. It outlines a structured learning path with modules and linked resources.

```markdown
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

Good luck with your learning journey!
```

*(Note: The exact resources and structure will vary based on the topic input and real-time search results.)*

## 📚 Resources and References

- **CrewAI Documentation:** [https://docs.crewai.com/](https://docs.crewai.com/)
- **Google AI for Developers:** [https://ai.google.dev/](https://ai.google.dev/)
- **DuckDuckGo Search Library:** [https://pypi.org/project/duckduckgo-search/](https://pypi.org/project/duckduckgo-search/)
- **[Optional: Link to your GitHub repository where this code resides]**
- **[Optional: Link to your personal website or social media profile]**

## 📝 License

This project is licensed under the **MIT License**. See the LICENSE file for details [if you create one].