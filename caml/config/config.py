import os
import yaml

CONFIG_FILE_NAME = "config.json"
CONFIG_FOLDER_NAME = ".caml"


class Config:
    def __init__(self):
        self.config_exists = False
        self.config_folder_path = os.path.join(os.path.expanduser("~"), CONFIG_FOLDER_NAME)
        self.config_file_path = os.path.join(self.config_folder_path, CONFIG_FILE_NAME)

        if os.path.exists(self.config_folder_path) and os.path.exists(self.config_file_path):
            # Load the config file
            config = yaml.safe_load(open(self.config_file_path, "r")) or {}

            self._user = config.get("user", None)
            self._token = config.get("token", None)
            self._version = config.get("version", None)
            self._caml_url = config.get("caml_url", None)

    @property
    def user(self):
        return self._user

    @property
    def token(self):
        return self._token

    @property
    def version(self):
        return self._version

    @property
    def caml_url(self):
        return self._caml_url