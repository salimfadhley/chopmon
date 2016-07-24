import unittest

from chopmon import registry

class TestRegister(unittest.TestCase):

    def test_register_empty(self):

        # @registry.register
        # def foo():
        #     return "Hi!"

        self.assertEqual(registry.get_functions("all"), set())

    def test_register_single_function(self):

        @registry.register
        def foo():
            return "Hi!"

        self.assertEqual(registry.get_functions("all"), set([foo]))