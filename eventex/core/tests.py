from django.test import TestCase

class SettingsTestCase(TestCase):
    def test_simple_to_test_travisci_integration(self):
        self.assertEqual(1,2)