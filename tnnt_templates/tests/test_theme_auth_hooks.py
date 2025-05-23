"""
Tests for the theme auth hooks
"""

# Standard Library
from unittest.mock import patch

# Django
from django.test import TestCase

# AA Templates: Terra Nanotech
from tnnt_templates.theme.terra_nanotech import auth_hooks


class TerraNanotechThemeHookTests(TestCase):
    """
    Test the theme hook
    """

    def setUp(self):
        """
        Set up the test

        :return:
        :rtype:
        """

        self.theme_hook = auth_hooks.TerraNanotechThemeHook()

    def test_should_have_correct_name_and_description(self):
        """
        Test should have the correct name and description

        :return:
        :rtype:
        """

        self.assertEqual(first=self.theme_hook.name, second="Terra Nanotech")
        self.assertEqual(
            first=self.theme_hook.description, second="Terra Nanotech Corp Auth Theme"
        )

    def test_should_have_correct_number_of_css_and_js_files(self):
        """
        Test should have the correct number of css and js files

        :return:
        :rtype:
        """

        self.assertEqual(first=len(self.theme_hook.css), second=8)
        self.assertEqual(first=len(self.theme_hook.js), second=4)

    def test_should_have_correct_header_padding(self):
        """
        Test should have correct header padding

        :return:
        :rtype:
        """

        self.assertEqual(first=self.theme_hook.header_padding, second="3.5em")

    @patch("tnnt_templates.theme.terra_nanotech.auth_hooks.TerraNanotechThemeHook")
    def test_should_register_theme_hook(self, mock_theme_hook):
        """
        Test should register theme hook

        :param mock_theme_hook:
        :type mock_theme_hook:
        :return:
        :rtype:
        """

        auth_hooks.register_terra_nanotech_hook()
        mock_theme_hook.assert_called_once()
