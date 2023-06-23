import json
import os


class ConfigurationSettings:
    def __init__(self, config_path):
        self.config_path = config_path

    def read_config(self):
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)

    def update_config(self, new_config):
        with open(self.config_path, 'w') as config_file:
            json.dump(new_config, config_file, indent=4)
