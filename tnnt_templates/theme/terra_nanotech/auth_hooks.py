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
            self=self,
            name="Terra Nanotech",
            description="Terra Nanotech Corp Auth Theme",
            html_tags={"data-theme": "terra-nanotech"},
            css=[
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url="tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.3/css/bootstrap.min.css",
                    ),
                    "integrity": "sha512-lF+xS8uroqRohnQyVXSTrsB+YgYcwHKVm8T6atFzc/cnOW1RTnc6x00585jS74sz9GPrNbzH4QkP8JICSXNP0Q==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url=f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-defaults.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-YxT6QJL/XZt9AoLDnb3nL2NH73+fWFckEIA8v2wXqr0nGxjWBKhXL4iVGOFiXkQ8Avj+3/JGrK5kl86M4XokwA==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url=f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-fonts.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-mF/lpSPp8ihS9XOtcOPAFzpzsQRMKH3D0scCPEKIaTpVtDd7F6iIafkdkD1VJ1ubsQKy3CUiBWigoVKE62TlXQ==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url="tnnt_templates/libs/fira-code/6.2.0/fira_code.min.css",
                    ),
                    "integrity": "sha512-kb4iEbG2cLDSYtf9DwOhdfrkxZnsZM+Ce+S+ZncKJJMNszS4JmqOk/EIoK0nCMskKiBb1Dmlg+i/fyR5SRJmQg==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url="tnnt_templates/libs/highlight-js/11.10.0/styles/default.min.css",
                    ),
                    "integrity": "sha512-hasIneQUHlh06VNBe7f6ZcHmeRTLIaQWFd43YriJ0UND19bvYRauxthDg8E4eVNPm9bRUhr5JGeqH7FRFXQu5g==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url=f"tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-S5OsDPsewG4OjFEcgG9yTHwgxI3Z3l0B05MHZjyDbz7tAo0JjWXYm+9OhQRU9cBkr96ZYpubVwoplKUEYqtT2w==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url=f"tnnt_templates/theme/terra-nanotech/aav4/css/community-app-fixes.min.css?v={__version__}",
                    ),
                    "integrity": "sha512-eMhTE194HJ5QO0aah3m/A1baNM52sGXViJLlhc8XYN5Hr7zZabbXPpG0DOLSLG4u+JbM/YBv22eUygGWJqmEEg==",
                },
            ],
            js=[
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url="tnnt_templates/theme/terra-nanotech/aav4/libs/popper/v2.11.8/popper.min.js",
                    ),
                    "integrity": "sha512-fhcY1KxngNJ4jVhZBdmrLv4/NH31jrNM45fpxytokYp06cd7Ug05E3gximUQmukhES9Xf0kbV5F1nHVqWq2bvQ==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url="tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.3/javascript/bootstrap.min.js",
                    ),
                    "integrity": "sha512-gNyiMtmOs5iIO2fjMFZRSR1s9Espoi+fdDtNuSh1iMpeRminsho2AA7767qpfkYqskd9PtUfMwAg0KdKJsMTuQ==",
                },
                {
                    "url": urljoin(
                        base=settings.STATIC_URL,
                        url=f"tnnt_templates/javascript/terra-nanotech.min.js?v={__version__}",
                    ),
                    "js_type": "module",
                    "integrity": "sha512-vAFEkWP9xGuYDUYlgAhYFuVmqno1vgPVquNZ/pCO/bLfYVhQ7zZT62eJYk1aPSe6oszhsWrTtcCmnODQyfV2Dw==",
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
