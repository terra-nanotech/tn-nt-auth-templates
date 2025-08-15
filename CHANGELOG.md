# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
-->

## [In Development] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

### Added

- Bootstrap tooltips to `package_monitor` templates
- Transition animation to overflow changes
- Overflow detection and monitoring
- Border radius to active menu items

### Fixed

- HighlightJS copy code button size and position
- Some transparencies

### Removed

- Task queue status widget updates via AJAX, as it is now provided by Alliance Auth

## [3.11.1] - 2025-08-14

### Fixed

- ESI logo height in ESI Status Dashboard widget

## [3.11.0] - 2025-08-14

### Added

- Task queue status widget updates via AJAX

### Fixed

- Some CSS background overrides

### Changed

- Minimum requirements
  - Alliance Auth >= 4.9.0

## [3.10.0] - 2025-08-05

### Added

- Background override for AA SRP bulk action window

### Changed

- `fittings` templates overhaul

### Removed

- Icons and buttons to add character and change main character
  from the top menu and the dashboard. Adding characters should be done through
  the Character Audit

## [3.9.1] - 2025-07-27

### Added

- More tests

### Fixed

- Size and position of the ESI logo in the ESi Status Dashboard widget

## [3.9.0] - 2025-07-04

### Added

- Django checks for the 2 most important settings

### Changed

- Make use of the new `AaManifestStaticFilesStorage` storage class for static files
- Minimum dependencies:
  - `allianceauth>=4.8.0`

## [3.8.6] - 2025-06-27

### Changed

- Package Monitor templates to show only sections that are necessary
- Icon alignment on login page
- Use `sri_static` wherever possible

## [3.8.5] - 2025-06-17

### Changed

- Login page improved by adding the site name and logo to it

## [3.8.4] - 2025-06-16

### Fixed

- Login box appearance on mobile devices

## [3.8.3] - 2025-06-16

### Added

- Background image matching the EVE Online Legion expansion

## [3.8.2] - 2025-06-16

### Fixed

- AA Sov Timer contrast changes in v2.4.2

## [3.8.1] - 2025-06-13

### Added

- Template for ESI token selection

### Fixed

- `input-group-text` style
- HighlightJS for BS3 template fallback

### Changed

- Package Monitor templates improved

## [3.8.0] - 2025-05-24

### Added

- Copy to clipboard button to highlighted code blocks

### Fixed

- Code styling
- Stylelint issues (Expected "rgba" to be "rgb" (color-function-alias-notation))

### Changed

- `fittings` templates updated
- Some CSS tweaks
  - `card-title` now enforces a `margin-bottom: 0;`
  - Fixes to various form elements margins
- Templates for `aa-package-monitor` updated to match v2.1.0
- Wording for the redirect message after registration
- Dependencies
  - `allianceauth>=4.7.0`

### Removed

- `corptools` template overrides, as they are now provided by the app
- Workaround for the Bootstrap 5 base template
- Obsolete settings

## [3.7.10] - 2025-03-24

### Fixed

- Scrollbar positioning in content area
- `logo_height` variable name

## [3.7.9] - 2025-03-18

### Added

- Site name and URL to OpenGraph tags

### Fixed

- Top navigation inner padding
- OpenGraph meta tag syntax

## [3.7.8] - 2025-03-18

### Added

- Temporary workaround for OpenGraph tags until the merge request is merged and released
  ([Alliance Auth/1701](https://gitlab.com/allianceauth/allianceauth/-/merge_requests/1701))

## [3.7.7] - 2025-02-28

### Fixed

- Button size in fittings menu

### Removed

- Border from navbar menu items

## [3.7.6] - 2025-02-25

### Fixed

- Progressbar keyframes

## [3.7.5] - 2025-02-25

### Changed

- Updated the `fittings` templates to Bootstrap 5

## [3.7.4] - 2025-02-24

### Added

- Corptools skill checks to fittings view

## [3.7.3] - 2025-02-23

### Changed

- Some colour corrections

## [3.7.1] - 2025-02-22

### Fixed

- Tooltip flicker in CorpTools ([CorpTools#117](https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools/issues/117))

## [3.7.0] - 2025-02-15

### Removed

- `corpstats` templates

## [3.6.0] - 2025-01-26

### Changed

- Use `django-sri` for hash calculation
- Highlight for active menu items in the sidebar menu improved

## [3.5.1] - 2025-01-20

### Fixed

- Datatable translations
- Missing `li` tags

## [3.5.0] - 2025-01-12

### Added

- Management command to anonymize all user's email addresses in the database
  ```shell
  python manage.py tnnt_anonymize_emails
  ```
  This will replace each user's email address with `user_id@domain.tld` (e.g. `371@my.auth.com`)

### Fixed

- JS issues with the BS3 fallback

### Changed

- `corpstat` templates updated for Bootstrap 5

## [3.4.1] - 2024-12-17

### Changed

- Don't ask for an email when `REGISTRATION_VERIFY_EMAIL` is set to `False`

## [3.4.0] - 2024-12-10

### Changed

- Make `init` function in main JS file self-executing
- `blacklist` templates updated
- highlight.js updated to v11.10.0
- Code block detection for `highlight.js` improved
- Minimum dependencies:
  - `allianceauth>=4.5.0`

### Removed

- Bundled ChartJS, as it was not used

## [3.3.0] - 2024-09-09

### Added

- AAv4 template overrides for `aa-package-monitor`

### Changed

- The minimum required AA version is now 4.3.0
- Use new CSS styling for the forum SVG icons

### Removed

- Template overrides for `allianceauth-securegroups`

## [3.2.0] - 2024-07-15

### Fixed

- Search icon color for global search on `forum` app

### Changed

- Button size slightly adjusted

### Removed

- Support for Python 3.8 and Python 3.9

## [3.1.0] - 2024-06-27

### Fixed

- Overflow detection for the Characters and Membership panel on the dashboard
- Search icon color in the top menu

### Removed

- Bootstrap 3 templates for Mumble Temps

## [3.0.2] - 2024-04-03

### Fixed

- Link color in CKEditor

### Changed

- Versioning own CSS and JS

## [3.0.1] - 2024-04-03

### Fixed

- Blockquote padding
- Code blocks and code highlighting

## [3.0.0] - 2024-03-16

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance before
> you install this version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> **This version is not compatible with Alliance Auth v3.x!**
>
> For versions compatible with Alliance Auth v3.x, see the [Releases](https://github.com/terra-nanotech/tn-nt-auth-templates/releases) before v3.0.0.

### Added

- Compatibility with Alliance Auth v4.0.0

### Removed

- Compatibility with Alliance Auth v3.x

## [3.0.0-rc.1] - 2024-03-12

> [!NOTE]
>
> **This version needs at least Alliance Auth v4!**
>
> Please make sure to update your Alliance Auth instance before
> you install this version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> **This version is not compatible with Alliance Auth v3.x!**
>
> For versions compatible with Alliance Auth v3.x, see the [Releases](https://github.com/terra-nanotech/tn-nt-auth-templates/releases) before v3.0.0.

### Fixed

- CSS paths in `mumbletemps` public template for the BS3 fallback

### Changed

- Updated to Bootstrap 5.3.3

## [3.0.0-beta.3] - 2024-03-10

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0b2!**
>
> Please make sure to update your Alliance Auth instance before
> you install this version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> **This version is not compatible with Alliance Auth v3.x!**
>
> For versions compatible with Alliance Auth v3.x, see the [Releases](https://github.com/terra-nanotech/tn-nt-auth-templates/releases) before v3.0.0.

### Added

- Integrity checks for the CSS and JS files

### Fixed

- `.navbar-brand` padding and margin

## [3.0.0-beta.2] - 2024-02-29

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0b2!**
>
> Please make sure to update your Alliance Auth instance before
> you install this version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> **This version is not compatible with Alliance Auth v3.x!**
>
> For versions compatible with Alliance Auth v3.x, see the [Releases](https://github.com/terra-nanotech/tn-nt-auth-templates/releases) before v3.0.0.

### Added

- Overflow detection to the Membership panel on the dashboard

### Changed

- CSS improved for overflowing elements

## [3.0.0-beta.1] - 2024-02-28

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0b2!**
>
> Please make sure to update your Alliance Auth instance before
> you install this version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> **This version is not compatible with Alliance Auth v3.x!**
>
> For versions compatible with Alliance Auth v3.x, see the [Releases](https://github.com/terra-nanotech/tn-nt-auth-templates/releases) before v3.0.0.

### Added

- Compatibility with Alliance Auth v4.0.0

### Removed

- Compatibility with Alliance Auth v3.x

## [2.12.0] - 2023-10-13

### Fixed

- Task count on dashboard

### Changed

- Minimum dependencies:
  - `allianceauth>=3.7.0`

## [2.11.7] - 2023-09-21

### Fixed

- Sanitise settings from `local.py`
- Some faulty open-graph tags

### Changed

- Minimum dependencies:
  - `allianceauth>=3.6.1`
  - `allianceauth-app-utils>=1.20.1`
- Test environment for `tox` cleaned up

## [2.11.6] - 2023-09-17

### Added

- JS compression and CSS/JS source maps

## [2.11.5] - 2023-09-01

### Fixed

- Styles for AA Intel Tool

## [2.11.4] - 2023-08-13

### Fixed

- AA Bootstrap fixes

## [2.11.3] - 2023-08-10

### Fixed

- Highlight CSS classes for AA Intel Tool

## [2.11.2] - 2023-08-08

### Fixed

- Allow system messages also for non-logged-in users

## [2.11.1] - 2023-08-08

### Fixed

- Missing message icon

## [2.11.0] - 2023-08-08

### Changed

- Main template adapted for AA's new public views feature

## [2.10.0] - 2023-08-01

### Changed

- Adapted for Alliance Auth v3.6.0

## [2.9.2] - 2023-07-30

### Added

- Styles for app footer

### Changed

- Moved the build process to PEP 621 / pyproject.toml

### Removed

- Translation files, makes no sense in a template override

## [2.9.1] - 2023-04-20

### Fixed

- Added missing `readonly` attribute to EFT fitting

## [2.9.0] - 2023-04-20

### Changed

- Templates for the `fittings` module adapted for v2.0.0 of the module

## [2.8.1] - 2023-03-18

### Changed

- Colors for code blocks updated

## [2.8.0] - 2022-10-14

### Added

- Token Management page and menu item (AA 3.3.0 | See: https://gitlab.com/allianceauth/allianceauth/-/issues/1356)

### Changed

- Minimum Requirements
  - Alliance Auth >= 3.3.0

## [2.7.7] - 2022-09-09

### Fixed

- Use the right markup for the celery progress bar

## [2.7.6] - 2022-09-04

### Changed

- Backdrop effect for modal windows (Part 2)

## [2.7.5] - 2022-09-04

### Changed

- Backdrop effect for modal windows

## [2.7.4] - 2022-09-01

### Added

- CSS overrides for AA Forum's Personal Messages feature

## [2.7.3] - 2022-08-28

### Fixed

- Pending button in secure groups is now correctly displayed
- "Leave Requests" tab in group management is now hidden as it should when
  `GROUPMANAGEMENT_AUTO_LEAVE = True`

## [2.7.2] - 2022-08-25

### Changed

- CSS to match `aa-forum` v1.13.0

## [2.7.1] - 2022-08-25

### Changed

- Split SVG Icons for dark/light mode and better icon names to match the changes in
  v1.12.0 of `aa-forum`

## [2.7.0] - 2022-08-25

### Added

- Cleaned up templates for `allianceauth-blacklist`
- HTML bundles for Chart-JS, In case one of the templates we override needs it and
  is loading it from a CDN (GDPR Issue)
- Override for `aa-forum` SVG icons

## [2.6.3] - 2022-08-09

### Changed

- Moved OpenGraph tags to their own template, so they can be overridden with a
  simple template override in by copying
  [this file](tnnt_templates/templates/tnnt_templates/opengraph-tags.html) to:
  ```
  myauth/myauth/templates/tnnt_templates/includes/opengraph-tags.html
  ```

## [2.6.2] - 2022-08-08

### Added

- Styles for [AA Discord Announcements](https://github.com/ppfeufer/aa-discord-announcements)

## [2.6.1] - 2022-08-06

### Changed

- Styles for AA-SRP
- Darkmode CSS variables
- CSS stylelint applied

## [2.6.0] - 2022-07-30

**This release is for Alliance Auth v3.0.0b3 or higher. Do not try and attempt to
run it with any version prior!**

### Fixed

- Templates for `mumbletemps`
- Use our own eve-time js in `mumbletemps` public-facing template
- HTML Syntax in several templates
- Left margin for AA Forum in mobile view
- Left margin for AFAT in mobile view
- Left margin for AA SRP in mobile view
- Left margin for AA Sovereignty Timer in mobile view
- Left margin for AA Bulletin Board in mobile view
- Left margin for AA Memberaudit in mobile view
- "Pending" button on the groups page
- Use AA's bundled versions of JavaScripts it provides

### Added

- Hide placeholders in form elements when they are being focused
- Blur effect to the fixed top navigation bar
- CSS variables
- Background blur instead of transparency
- Missing Favicons

### Changed

- Bottom border colors for SRP payout values
- CSS color values modernized
- Minimum requirement
  - Alliance Auth >= 3.0.0

### Removed

- No longer used templates
- Tests and guaranteed compatibility with AA below v3.0.0
- `type="application/javascript"` from script-tags, as it is deprecated
- `type="text/css"` from style-tags, as it is deprecated

## [2.6.0-beta.3] - 2022-07-19

**This release is for Alliance Auth v3.0.0b3 or higher. Do not try and attempt to
run it with any version prior!**

### Fixed

- Templates for `mumbletemps`
- Use our own eve-time js in `mumbletemps` public-facing template
- HTML Syntax in several templates

### Added

- Hide placeholders in form elements when they are being focused

### Changed

- CSS color values modernized

### Removed

- No longer used templates

## [2.6.0-beta.2] - 2022-07-16

**This release is for Alliance Auth v3.0.0b3 or higher. Do not try and attempt to
run it with any version prior!**

### Fixed

- Left margin for AA Forum in mobile view
- Left margin for AFAT in mobile view
- Left margin for AA SRP in mobile view
- Left margin for AA Sovereignty Timer in mobile view
- Left margin for AA Bulletin Board in mobile view
- Left margin for AA Memberaudit in mobile view

## [2.6.0-beta.1] - 2022-07-16

**This release is for Alliance Auth v3.0.0b3 or higher. Do not try and attempt to
run it with any version prior!**

### Fixed

- "Pending" button on the groups page
- Use AA's bundled versions of JavaScripts it provides

### Added

- Blur effect to the fixed top navigation bar
- CSS variables
- Background blur instead of transparency
- Missing Favicons

### Removed

- Unused template
- Tests and guaranteed compatibility with AA below v3.0.0
- `type="application/javascript"` from script-tags, as it is deprecated
- `type="text/css"` from style-tags, as it is deprecated

### Changed

- Minimum requirement
  - Alliance Auth >= 3.0.0b3

## [2.5.4] - 2022-05-12

### Added

- Template for admin task status bar

### Changed

- Minimum requirement
  - Alliance Auth >= 2.12.0

## [2.5.3] - 2022-05-09

### Changed

- Templates for `structuretimers` to match the latest version

## [2.5.2] - 2022-03-20

### Changed

- Template `allianceauth/admin-status/overview.html` to match the latest version
- Minimum requirement
  - Alliance Auth >= 2.11.1

## [2.5.1] - 2022-03-03

### Fixed

- `$(this)` in JS arrow function

## [2.5.0] - 2022-03-03

### Added

- Test suite for AA 3.x and Django 4

### Changed

- Link "Latest Stable" and "Latest Pre-Release" versions to their tags on GitLab
- Switched to `setup.cfg` as config file, since `setup.py` is deprecated now

### Removed

- Deprecated settings

## [2.4.2] - 2022-02-26

### Changed

- Task overview tweaked to get more information
- Minimum requirement
  - Alliance Auth >= 2.11.0

## [2.4.1] - 2022-02-26

### Changed

- Templates changed to match AA v2.11.0

## [2.4.0] - 2022-02-20

### Fixed

- Use proper HTML5 tags instead of self-closing XML/(X)HTML tags
- Remove deprecated `xlink` notation for SVG
- Use `{% static "" %}` instead of hardcoded image url in fittings templates

### Changed

- Show "Fitting Notes" box only if there are fitting notes
- JavaScript modernised

## [2.3.3] - 2022-01-25

### Changed

- Switched to `setInterval()` to render the EVE time

## [2.3.2] - 2022-01-22

### Changed

- Main JS cleaned up

## [2.3.1] - 2022-01-19

### Fixed

- Template for `structuretimers` to match with the latest changes in v1.2.0

## [2.3.0] - 2022-01-12

### Added

- Tests for Python 3.11
- Seconds to EVE time in header

### Changed

- JavaScript: `const` instead of `let` where appropriate
- Minimum requirements
  - Alliance Auth v2.9.4

## [2.2.0] - 2021-12-07

### Changed

- Fira Code updated to v6.2.0

## [2.1.0] - 2021-11-30

### Changed

- Minimum requirements
  - Alliance Auth v2.9.3

## [2.0.4] - 2021-11-27

### Added

- Tests for template tags
- Missing `tr` tag

### Changed

- License updated to GPLv3
- Minimum dependencies versions

## [2.0.3] - 2021-11-04

### Changed

- Optimer templates updated to match changes in AA 2.9.1

## [2.0.2] - 2021-10-19

### Changed

- Use SITE_NAME variable instead of a static site name

## [2.0.1] - 2021-10-18

### Fixed

- Page titles

## [2.0.0] - 2021-10-17

Changed

- Release for AA 2.9.0

## [2.0.0-beta.2] - 2021-10-08

### Important

**This release is for Alliance Auth v2.9.0b1 or higher. Do not try and attempt to
run it with any version prior!**

### Changed

- Public template for `mumbletemps` changed for AA 2.9.0

## [2.0.0-beta.1] - 2021-09-28

### Important

**This release is for Alliance Auth v2.9.0b1 or higher. Do not try and attempt to
run it with any version prior!**

### Changed

- User menu min width set to 225px

## [1.8.0] - 2021-09-19

### Important

**This release is for Alliance Auth v2.9.0b1 or higher. Do not try and attempt to
run it with any version prior!**

### Changed

- Top Menu adapted for AA's new top menu structure

### Fixed

- CSS for SumoSelect field in `aa-bulletin-board`

## [1.7.7] - 2021-08-15

### Fixed

- Check for forum URLs

## [1.7.6] - 2021-08-14

### Fixed

- jQuery code should always be wrapped in document.ready()

## [1.7.5] - 2021-08-11

### Changed

- Templates for `allianceauth-securegroups-0.1.0`

## [1.7.4] - 2021-08-06

### Changed

- `.panel-body` min-height removed

## [1.7.3] - 2021-08-04

### Changed

- Adjusted the font-size for `blockquote` to 0.95rem

## [1.7.2] - 2021-08-02

### Changed

- CSS for AA Forum v0.1.0-beta.14

## [1.7.1] - 2021-07-24

### Changed

- CSS for AA Forum v0.1.0-beta.11

## [1.7.0] - 2021-07-20

### Added

- Detection for forum links to change meta tags accordingly

### Changed

- Path to login SVG

## [1.6.4] - 2021-07-20

### Changed

- CSS for AA Forum v0.1.0-beta.10

### Removed

- Files from an earlier version that are no longer needed

## [1.6.3] - 2021-07-19

### Fixed

- timer_list template for `structuretimers`

## [1.6.2] - 2021-07-16

### Changed

- CSS for `aa-forum` to better position the search bar in the navigation

### Removed

- YouTube plugin for CKEditor, it's served with `aa-forum` and `aa-bulletin-board`

## [1.6.1] - 2021-07-14

### Changed

- Templates for `aa-structuretimers` to conform with v1.1.0

## [1.6.0] - 2021-07-11

### Removed

- Discordbot Cogs. They have been moved to its own app »
  [TN-NT Discordbot Cogs](https://github.com/terra-nanotech/tn-nt-discordbot-cogs)

## [1.5.23] - 2021-07-10

### Changed

- Discord cogs for AA-Discordbot v0.5.2

## [1.5.22] - 2021-07-09

### Changed

- Discord cogs for AA-Discordbot v0.5.1

## [1.5.21] - 2021-07-08

### Changed

- CSS for AA Forum (hover for sticky and locked topics to match their original
  background color)

## [1.5.20] - 2021-06-30

### Fixed

- Table width for corpstats view

## [1.5.19] - 2021-06-28

### Added

- Proper favicons

## [1.5.18] - 2021-06-28

### Added

- Fira Code font for `<code>` blocks
- New and better alert messages
- YouTube plugin for ckEditor. Activate by adding the following to your ckEditor
  configuration in your `local.py`
  ```python
  CKEDITOR_CONFIGS = {
      "default": {
          "youtube_responsive": True,
          "youtube_privacy": True,
          "youtube_related": False,
          "extraPlugins": ",".join(
              [
                  "youtube",
              ]
          ),
      }
  }
  ```

### Changed

- CSS for [AA Forum](https://github.com/ppfeufer/aa-forum) app to match its upcoming
  alpha release (v0.0.1-alpha.10)

## [1.5.17] - 2021-06-17

### Changed

- CSS for [AA Forum](https://github.com/ppfeufer/aa-forum) app to match its current
  alpha release (v0.0.1-alpha.9)

## [1.5.16] - 2021-06-14

### Fixed

- Top margin on topic list for AA Forum

## [1.5.15] - 2021-06-14

### Fixed

- Hover state for topics in board view (AA Forum)

## [1.5.14] - 2021-06-13

### Changed

- Bottom margin on paragraphs set to 1rem

## [1.5.13] - 2021-06-12

### Changed

- CSS for [AA Forum](https://github.com/ppfeufer/aa-forum) app to match its current
  alpha release (v0.0.1-alpha.4)

## [1.5.12] - 2021-06-11

### Added

- CSS styles for [AA Forum](https://github.com/ppfeufer/aa-forum) app

## [1.5.11] - 2021-06-01

# Fixed

- Order of JavaScript functions in `mumbletemps` public template

### Added

- JavaScript to display EVE time in the top menu

## [1.5.10] - 2021-05-27

### Fixed

- Top margin for `mumbletemps` public invite template

## [1.5.9] - 2021-05-19

### Fixed (now as well for AA 2.8.x and not only for the alpha version)

- Define function before use in javascript
- Background in ckEditor

## [1.5.8] - 2021-05-17

### Fixed

- Define function before use in javascript

## [1.5.7] - 2021-05-17

### Fixed

- Background in ckEditor

### Changed

- JS in templates modernized

## [1.5.6] - 2021-05-05

### Fixed

- Using Django application registry instead of directly accessing `INSTALLED_APPS`

## [1.5.5] - 2021-04-23

### Added

- EVE time to top menu bar
- Bootstrap JS to Mumble Temp public template

## [1.5.4] - 2021-04-22

### Added

- Link to support Discord to admin notifications paned on dashboard
- JS libraries used by Fittings and Doctrines module, so we don't have to use
  cloudflare CDN here
- CSS for ckeditor

### Changed

- Templates for AFAT release 2.0.0
- Link ship icon in doctrine view to open fitting
- Link ship icon in all fittings view to open fitting
- Templates for Fittings and Doctrines module, so they don't use cloudflare CDN

## [1.5.3] - 2021-03-24

### Changed

- Mapping removed

## [1.5.2] - 2021-03-23

### Changed

- price check code optimized

## [1.5.1] - 2021-03-23

### Added

- `!jita` and `!amarr` commands to price lookups

### Changed

- Price check code optimized

## [1.5.0] - 2021-03-23

### Added

- Price checks (Jita and Amarr) for the Discordbot

## [1.4.8] - 2021-03-16

### Added

- Add `target="_blank"` and `rel="noopener noreferer"` to external links

## [1.4.7] - 2021-03-16

### Fixed

- top positioning for `.aa-fleetpings-pingtext` box

## [1.4.6] - 2021-03-11

### Fixed

- django.template.exceptions.TemplateSyntaxError: Invalid filter:
  'alliance_logo_url' (Missing evelinks template tag)
- Page title translations

## [1.4.5] - 2021-03-10

### Changed

- Some text fixes for allianceauth-dicordbot

## [1.4.4] - 2021-03-08

### Changed

- Navbar is now sticky at the top

## [1.4.3] - 2021-03-04

### Fixed

- Respect Discord max payload length

## [1.4.2] - 2021-02-16

### Fixed

- Show alliance name in user menu only when there is an alliance

## [1.4.1] - 2021-02-11

### Changed

- Use the constant for the entity name where ever possible

### Fixed

- Template's overall image style also for entity logo on login/register

## [1.4.0] - 2021-02-11

### Changed

- Template settings

## [1.3.3] - 2021-02-08

### Fixed

- Corpstats overview table look and feel

## [1.3.2] - 2021-02-05

### Fixed

- Alliance name in corpstats

## [1.3.1] - 2021-02-05

### Fixed

- OG-Image syntax

## [1.3.0] - 2021-02-05

### Added

- Compatibility with the notification changes from upstream
  ([see here](https://gitlab.com/allianceauth/allianceauth/-/merge_requests/1218))
- Moved top menu into a user menu dropdown
- Common image style, no longer mix of `img-circle` and `img-rounded`
- Cog for auth commands for discordbot
- Cog for `!time` command added for discordbot
- Templates for [securegroups](https://github.com/pvyParts/allianceauth-secure-groups)

### Changed

- Entity logo made configurable

### Fixed

- Panel headers
- Table look and feel
- Fitting panel in doctrine view (fittings module)

## [1.2.6] - 2021-01-24

### Changed

- Set "Roboto" as the default font

## [1.2.5] - 2021-01-23

### Fixed

- AttributeError: 'NoneType' object has no attribute 'username'

## [1.2.4] - 2021-01-23

### Fixed

- Typo in configuration constant

## [1.2.3] - 2021-01-23

### Fixed

- `!timer` command allowed channels

## [1.2.2] - 2021-01-23

### Added

- Customized cogs for aadiscordbot

## [1.2.1] - 2021-01-20

### Added

- Explicit font color for navigation, because there are people who override that in
  their extension CSS ...

## [1.2.0] - 2021-01-18

### Added

- Templates for AFAT statistics to set the right font color on the canvas elements

## [1.1.3] - 2021-01-09

### Fixed

- django.template.exceptions.TemplateSyntaxError:
  Invalid block tag on line 22: 'translate"Ratio"', expected 'endblock'.

## [1.1.2] - 2021-01-06

### Added

- Template for mummbletemps invite page

### Fixed

- Table header on corpstats page

## [1.1.1] - 2020-12-27

### Changed

- Tables in Group and Grou Management views are now DataTables

## [1.1.0] - 2020.12.22

### Added

- Templates for AA Fleet

## [1.0.1] - 2020.12.20

### Added

- Hover and active style to nav-pills in panel-header

## [1.0.0] - 2020.12.19

### Added

- Own template for Terra Nanotech
- Template overrides for the external apps we use, to accommodate with the fixes to
  bootstrap we made

### Fixed

- Many wrongly used bootstrap classes and markup within the original Auth template

## [0.0.6] - 2020.12.14

### Fixed

- Missing `}` in a django template

## [0.0.5] - 2020.12.14

### Added

- Style for DataTables filter

### Fixed

- DataTables filter on corpstats
- Templates for fittings module

## [0.0.4] - 2020.12.13

### Added

- Fixes for AA's wrong usage of Bootstrap classes
- Template overrides for built-in functions to accommodate these fixes
- Template overrides for external apps we use

## [0.0.3] - 2020.12.13

### Changed

- Margins moved to elements that actually need them

## [0.0.2] - 2020.12.13

### Changed

- Group names on the dashboard are now nice labels instead of an ugly table

## [0.0.1] - 2020.12.10

### Added

- initial version for Alliance Auth >= 2.8.0
