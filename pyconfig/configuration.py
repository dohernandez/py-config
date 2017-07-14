import yaml
import os


class Configuration:
    def __init__(self, config_file, base_path=None):
        self.__configuration = {}

        self.load(config_file=config_file, base_path=base_path)

    def load(self, config_file, base_path=None):
        if not base_path:
            base_path = os.getcwd()

        configuration = yaml.load(open(
            os.path.join(base_path, config_file), 'r').read())

        if configuration:
            self.__configuration.update(configuration)

    def get_conf(self, key):
        if key in self.__configuration:
            return self.__configuration[key]
        else:
            return None

    def set_conf(self, key, value):
        self.__configuration.update({key: value})
