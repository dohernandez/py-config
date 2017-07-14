import os
import unittest2

from pyconfig.configuration import Configuration


class ConfigurationTest(unittest2.TestCase):
    def test_create_config(self):
        config = Configuration('config.yml', os.path.dirname(os.path.abspath(__file__)))

        self.assertEquals('Py Config Test', config.get_conf('app_name'))
