"""
Unit tests for TN-NT Template tags

This module contains unit tests for custom template tags used in the TN-NT Auth Theme.
The tests ensure that the template tags behave as expected under various conditions.
"""

# Standard Library
from unittest.mock import patch

# Django
from django.template import Context, Template

# AA Templates: Terra Nanotech
from tnnt_templates.templatetags.tnnt_templates import is_app_installed, startswith
from tnnt_templates.tests import BaseTestCase


class TestFilterStartsWith(BaseTestCase):
    """
    Unit test class for the `startswith` template filter.
    """

    def test_returns_true_when_haystack_starts_with_needle(self):
        """
        Tests that the `startswith` filter returns True when the haystack starts with the needle.

        :return:
        :rtype:
        """

        self.assertTrue(startswith("hello world", "hello"))

    def test_returns_false_when_haystack_does_not_start_with_needle(self):
        """
        Tests that the `startswith` filter returns False when the haystack does not start with the needle.

        :return:
        :rtype:
        """

        self.assertFalse(startswith("hello world", "world"))

    def test_returns_true_when_needle_is_empty(self):
        """
        Tests that the `startswith` filter returns True when the needle is an empty string.

        :return:
        :rtype:
        """

        self.assertTrue(startswith("haystack", ""))

    def test_returns_true_when_both_haystack_and_needle_are_empty(self):
        """
        Tests that the `startswith` filter returns True when both haystack and needle are empty strings.

        :return:
        :rtype:
        """

        self.assertTrue(startswith("", ""))

    def test_is_case_sensitive(self):
        """
        Tests that the `startswith` filter is case-sensitive.

        :return:
        :rtype:
        """

        self.assertFalse(startswith("Hello World", "hello"))

    def test_raises_type_error_when_needle_is_none(self):
        """
        Tests that the `startswith` filter raises a TypeError when the needle is None.

        :return:
        :rtype:
        """

        with self.assertRaises(TypeError):
            startswith("haystack", None)

    def test_raises_attribute_error_when_haystack_is_none(self):
        """
        Tests that the `startswith` filter raises an AttributeError when the haystack is None.

        :return:
        :rtype:
        """

        with self.assertRaises(AttributeError):
            startswith(None, "needle")

    def test_raises_attribute_error_for_non_string_haystack(self):
        """
        Tests that the `startswith` filter raises an AttributeError when the haystack is not a string.

        :return:
        :rtype:
        """

        with self.assertRaises(AttributeError):
            startswith(12345, "12")


class TestTagIsAppInstalled(BaseTestCase):
    """
    Unit test class for the `is_app_installed` template tag.
    """

    def test_returns_true_when_app_is_installed(self):
        """
        Tests that the `is_app_installed` filter returns True when the app is installed.

        :return:
        :rtype:
        """

        with patch(
            "tnnt_templates.templatetags.tnnt_templates.apps.is_installed",
            return_value=True,
        ) as mock_is_installed:
            result = is_app_installed("some_app")
            mock_is_installed.assert_called_once_with("some_app")

            self.assertTrue(result)

    def test_returns_false_when_app_is_not_installed(self):
        """
        Tests that the `is_app_installed` filter returns False when the app is not installed.

        :return:
        :rtype:
        """

        with patch(
            "tnnt_templates.templatetags.tnnt_templates.apps.is_installed",
            return_value=False,
        ) as mock_is_installed:
            result = is_app_installed("missing_app")
            mock_is_installed.assert_called_once_with("missing_app")

            self.assertFalse(result)

    def test_forwards_non_string_argument_to_apps_is_installed(self):
        """
        Tests that the `is_app_installed` filter returns True when the app is installed and forwards non-string arguments to `apps.is_installed`.

        :return:
        :rtype:
        """
        with patch(
            "tnnt_templates.templatetags.tnnt_templates.apps.is_installed",
            return_value=False,
        ) as mock_is_installed:
            value = 12345
            result = is_app_installed(value)
            mock_is_installed.assert_called_once_with(value)

            self.assertFalse(result)

    def test_integration_template_tag_retrieves_value_into_context(self):
        """
        Test integration

        :return:
        :rtype:
        """

        tpl = Template(
            '{% load tnnt_templates %}{% is_app_installed "myapp" as installed %}installed={{ installed }}'
        )

        with patch(
            "tnnt_templates.templatetags.tnnt_templates.apps.is_installed",
            return_value=True,
        ):
            rendered = tpl.render(Context({})).strip()

        self.assertIn("installed=True", rendered)
