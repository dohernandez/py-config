import os
import unittest2

from pyconfig.configuration import Configuration


class ConfigurationTest(unittest2.TestCase):
    def test_create_config(self):
        config = Configuration('config.yml', os.path.dirname(os.path.abspath(__file__)))

        self.assertEquals('Py Config Test', config.get_conf('app_name'))

    def test_add_key_config(self):
        config = Configuration('config.yml', os.path.dirname(os.path.abspath(__file__)))
        config.set_conf('new_config', 'New key config')

        self.assertEquals('Py Config Test', config.get_conf('app_name'))
        self.assertEquals('New key config', config.get_conf('new_config'))

    def test_update_key_config(self):
        config = Configuration('config.yml', os.path.dirname(os.path.abspath(__file__)))
        config.set_conf('app_name', 'New Py Config Test')

        self.assertEquals('New Py Config Test', config.get_conf('app_name'))

    def test_load_an_extra_config_file(self):
        config = Configuration('config.yml', os.path.dirname(os.path.abspath(__file__)))

        self.assertEquals('Py Config Test', config.get_conf('app_name'))

        config.load('another_config.yml', os.path.dirname(os.path.abspath(__file__)))

        self.assertEquals('Another Py Config Test', config.get_conf('app_name'))
        self.assertEquals('Py Config Test', config.get_conf('previous_app_name'))

