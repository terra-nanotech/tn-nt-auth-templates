# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [1.5.18] - Upcoming

### Added

- Fira Code font for `<code>` blocks
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

- JavaScript to display Eve time in the top menu


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

- Eve time to top menu bar
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
