import yaml
from os import path


def replace_yaml_placeholders(file, placeholders):
    """
    Iterates over a configuration files and replaces the placeholders
    @param file: [String] path to the configuration file
    @param placeholders: [Dict] configuration placeholders and values
    @return: [Dict] json representation of the correct configuration
    """
    with open(path.join(path.dirname(__file__), file)) as f:
        file_content = f.read()
        for key in placeholders:
            file_content = file_content.replace(f"{{{key}}}", placeholders[key])

    return yaml.safe_load(file_content)
