import os
import unittest
from my_code import *
import yaml


class MyFirstTest(unittest.TestCase):

    def setUp(self) -> None:
        working_directory = os.getcwd()
        path_to_config = os.path.join(working_directory, "config.yaml")
        with open(path_to_config, "r") as yaml_config_file:
            config_file_string = yaml.load(yaml_config_file, Loader=yaml.FullLoader)
        self.hello_string = config_file_string['Strings']['hello']
        self.order_1 = config_file_string['Orders']['order1']
        self.order_2 = config_file_string['Orders']['order2']

    def test_hello(self):
        self.assertEqual(self.hello_string, hello_world())

    def test_get_order(self):
        self.assertEqual(self.order_1, get_order())
        self.assertNotEqual(self.order_1, None)

    def test_is_order_valid(self):
        order1 = is_order_valid(self.order_1)
        order2 = is_order_valid(self.order_2)
        self.assertEqual(order1, True)
        self.assertEqual(order2, False)
