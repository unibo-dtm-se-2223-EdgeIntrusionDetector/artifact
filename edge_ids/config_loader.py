"""
Module responsible for loading configuration files.
"""

from typing import Dict, Any
import yaml

class ConfigLoader:
    """
    Responsible for loading configuration settings from YAML files.
    """

    # We disable this check because this class currently has a single responsibility
    # but might grow in the future.
    # pylint: disable=too-few-public-methods
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Loads a YAML configuration file and returns it as a dictionary.

        Args:
            config_path (str): The absolute or relative path to the YAML file.

        Returns:
            Dict[str, Any]: A dictionary containing the configuration parameters.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            yaml.YAMLError: If the file is not valid YAML.
        """
        # Explicitly set encoding to 'utf-8' to ensure cross-platform compatibility
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        return config
