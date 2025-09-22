"""
General Purpose utility modules with miscellaneous helper functions
"""

import json


class Utils:
    """
    exportable class with miscellaneous helper functions
    """
    @staticmethod
    def get_config(file="config.json"):
        """
        Reads Config.json
        :param file: name of the config file
        :return: dict: contents of the config file
        """
        with open(file, encoding='utf-8') as config_file:
            return json.load(config_file)
