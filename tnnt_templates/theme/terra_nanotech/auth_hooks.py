"""
Auth hooks for Terra Nanotech theme
"""

# Standard Library
from urllib.parse import urljoin

# Django
from django.conf import settings

# Alliance Auth
from allianceauth import hooks
from allianceauth.theme.hooks import ThemeHook

# AA Templates: Terra Nanotech
from tnnt_templates import __version__


class TerraNanotechThemeHook(ThemeHook):
    """
    Terra Nanotech Corp Auth Theme
    https://github.com/terra-nanotech/tn-nt-auth-templates/
    """

    def __init__(self):
        """
        Init
        """

        ThemeHook.__init__(
            self,
            "Terra Nanotech",
            "Terra Nanotech Corp Auth Theme",
            css=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.3/css/bootstrap.min.css",
                    ),
                    "integrity": "sha512-lF+xS8uroqRohnQyVXSTrsB+YgYcwHKVm8T6atFzc/cnOW1RTnc6x00585jS74sz9GPrNbzH4QkP8JICSXNP0Q==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-defaults.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-E8vMqXFN+EiyBKkt06o/x5rK+ZGQk8f8+jgWJX5ZKDoxjG4noss9lfS/cgp5/evqXRlmdhBT8IB8QToCPNbq3w==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-fonts.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-mF/lpSPp8ihS9XOtcOPAFzpzsQRMKH3D0scCPEKIaTpVtDd7F6iIafkdkD1VJ1ubsQKy3CUiBWigoVKE62TlXQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/libs/fira-code/6.2.0/fira_code.min.css",
                    ),
                    "integrity": "sha512-kb4iEbG2cLDSYtf9DwOhdfrkxZnsZM+Ce+S+ZncKJJMNszS4JmqOk/EIoK0nCMskKiBb1Dmlg+i/fyR5SRJmQg==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/libs/highlight-js/11.01/styles/default.min.css",
                    ),
                    "integrity": "sha512-3xLMEigMNYLDJLAgaGlDSxpGykyb+nQnJBzbkQy2a0gyVKL2ZpNOPIj1rD8IPFaJbwAgId/atho1+LBpWu5DhA==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-tSa74ZzRLfzDYBcPXfr6TsNlZL+tT5J7cmCxazl/MAkGbsN5QkfL3VuHIqwqflWqIroDv20wVrPaSqYwdAFknQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        f"tnnt_templates/theme/terra-nanotech/aav4/css/community-app-fixes.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-iOCuDIU9rUdO6uEUSYEtmydVzzHB0Wks1EFG/zuB14QTzUpLVUlfkZs7VEzUlYRh1rvDK2iZQq6qjP1xTY6ZJg==",
                },
            ],
            js=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/popper/v2.11.8/popper.min.js",
                    ),
                    "integrity": "sha512-fhcY1KxngNJ4jVhZBdmrLv4/NH31jrNM45fpxytokYp06cd7Ug05E3gximUQmukhES9Xf0kbV5F1nHVqWq2bvQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.3/javascript/bootstrap.min.js",
                    ),
                    "integrity": "sha512-gNyiMtmOs5iIO2fjMFZRSR1s9Espoi+fdDtNuSh1iMpeRminsho2AA7767qpfkYqskd9PtUfMwAg0KdKJsMTuQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/libs/highlight-js/11.01/highlight.min.js",
                    ),
                    "integrity": "sha512-W7EehcwtSbRF63FIQlXEOOd5mnq0Et0V0nUOvwcUvjnCKgOLLYbqriQxEQSp63sfrkryxIg/A/O8v8O18QwQCQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        f"tnnt_templates/javascript/terra-nanotech.min.js?v={__version__}",
                    ),
                    "integrity": "sha512-cywgfN2+W39b72Mrf9zwX5j6I7jXZmC1YKCVovhV9fD554ll2yMqE+3A4s06s+6lZOAT/rZY5WwDo6haie2ZzA==",
                },
            ],
            header_padding="3.6em",
        )


@hooks.register("theme_hook")
def register_terra_nanotech_hook():
    """
    Registers the Terra Nanotech theme hook

    :return:
    :rtype:
    """

    return TerraNanotechThemeHook()
