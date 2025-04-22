#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from learning_path_creator_crew.crew import LearningPathCreator
from learning_path_creator_crew.utils.utils import read_crew_settings, collect_user_input

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    try:
        # Load the crew configuration from a YAML file
        crew_config = 'config/settings.yaml'
        crew_config = read_crew_settings(crew_config)

        # collect user input for the crew execution.
        user_prompts = crew_config['user_prompts']
        inputs = collect_user_input(user_prompts)

        LearningPathCreator().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    learning_topic = input("What topic do you want to learn about? (e.g., 'Introduction to Quantum Computing', 'Learn Python Programming') ")
    inputs = {'topic': learning_topic,}
    try:
        LearningPathCreator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LearningPathCreator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    learning_topic = input("What topic do you want to learn about? (e.g., 'Introduction to Quantum Computing', 'Learn Python Programming') ")
    inputs = {'topic': learning_topic,}
    try:
        LearningPathCreator().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
