# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [1.3.0] - 2021-xx-xx

### Added

- Compatibility with the notification changes from upstream
  ([see here](https://gitlab.com/allianceauth/allianceauth/-/merge_requests/1218))
- Moved top menu into a user menu dropdown
- Common image style, o longer mix of `img-circle` and `img-rounded`
- Cog for auth commands for discordbot
- Cog for `!time` command added for discordbot

### Changed

- Entity logo made configurable

### Fixed

- Panels hrapplication templates


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
