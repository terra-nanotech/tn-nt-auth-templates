from .utils import clean_setting

# Attempt to load JS/CSS/Fonts from staticfiles when possible
# This does not guarantee no CDN usage
# App Developers may or may not respect this setting
USE_TNNT_TEMPLATES = clean_setting("USE_TNNT_TEMPLATES", False)
