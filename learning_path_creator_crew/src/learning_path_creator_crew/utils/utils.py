import yaml

def read_crew_settings(settings_yaml_path: str) -> dict:
    """
    This function takes the path to a YAML configuration file, adjusts the path 
    to include the relative directory structure, and loads the contents of the 
    file into a dictionary.
    Args:
        settings_yaml_path (str): Relative path to the crew configuration file.
    Returns:
        dict: A dictionary containing the crew settings loaded from the YAML file.
    Raises:
        FileNotFoundError: If the specified YAML file does not exist.
        yaml.YAMLError: If there is an error while parsing the YAML file.
    """

    # correct the path to the settings_yaml_path file
    settings_yaml_path = f'src/learning_path_creator_crew/{settings_yaml_path}'
    # Load the YAML file
    with open(settings_yaml_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    # Return the loaded data
    return data

def collect_user_input(user_prompts: dict) -> dict:
    """
    Collects user input based on a dictionary of prompts and returns the inputs as a dictionary.
    Args:
        user_prompts (dict): A dictionary where each key represents the input field name, and the value is a dictionary 
            containing the following keys:
            - 'message' (str): The prompt message to display to the user.
            - 'default' (str, optional): The default value to use if the user provides no input. Defaults to an empty string.
            - 'user_input' (bool, optional): A flag indicating whether user input is required. If False, only the message 
              is displayed without prompting for input. Defaults to True.
    Returns:
        dict: A dictionary containing the collected inputs, where the keys match the keys from `user_prompts` and the 
        values are the user-provided or default values.
    Raises:
        Exception: If a mandatory input is not provided and no default value is specified.
    Behavior:
        - Prompts the user for input based on the provided `user_prompts` dictionary.
        - If the user provides no input and a default value is specified, the default value is used.
        - Displays a summary of the collected inputs and allows the user to restart the input process if desired.
    """
    inputs = {}
    summary = []

    for key, val in user_prompts.items():
        message = val['message'].strip()
        default_value = val.get('default', '') 
        user_input = val.get('user_input', True) 

        # if this is a mandatory input, we need to ask for it
        if user_input:
            print('-'*50)
            reply = input(f"{message}: ")
            if reply == "": 
                if default_value == "":
                    raise Exception("No input provided for one of the mandatory crew inputs.")
                else:
                    print(f"Default value will be used: {default_value}")
                    reply = default_value
            inputs[key] = reply
            summary.append(f"{key.title().replace('_', ' ')}: {reply}")
        else: # this is only a message, no input is required
            print(message)

    # show a summary of the inputs
    if len(summary) > 0:
        print(f"{'='*20} Summary of crew inputs {'='*20}")
        print("\n".join(summary))
        print("="*50)
        # ask the user if they want to start over
        start_over = input("\nPress [Enter] to accept or type [restart] to start over\n")
        if start_over.strip().lower() == "restart":
            print("Restarting...")
            return collect_user_input(user_prompts)
    return inputs
