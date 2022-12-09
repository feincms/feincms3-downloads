==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

.. _Next version: https://github.com/matthiask/feincms3-downloads/compare/0.5...main

- Fixed a tranlsation.

`0.5`_ (2022-09-28)
~~~~~~~~~~~~~~~~~~~

.. _0.5: https://github.com/matthiask/feincms3-downloads/compare/0.4...0.5

- Added ``DownloadBase.basename`` and
  ``DownloadBase.caption_or_basename`` properties.
- Switched to a declarative setup.
- Switched from Travis CI to GitHub actions.
- Raised the minimum version requirements to Django 3.2, Python 3.8. Added
  Python 3.10, Django 4.0 and 4.1.
- Started using pre-commit.


`0.4`_ (2020-08-13)
~~~~~~~~~~~~~~~~~~~

- Added Django checks verifying that the required binaries are installed
  and executable.
- Removed the assumption that files are accesssible using local file
  paths.
- Dropped compatibility with Python<3.6 and Django<2.2, verified
  compatibility with newer Python and Django versions.


`0.3`_ (2019-12-19)
~~~~~~~~~~~~~~~~~~~

- Extracted the preview JPEG generation into its own function.
- Modified the preview generation to never upscale images and to apply a
  bounding box instead of specifying only the maximum width.
- Changed the PDF preview generation to use pdftocairo from
  poppler-utils instead of convert from ImageMagick to avoid problems
  because of changes which were designed to limit PostScript vulnerabilities.


`0.2`_ (2016-09-18)
~~~~~~~~~~~~~~~~~~~

- Added an automatically managed ``file_size`` field to the plugin.
- Formatted the code using black.
- Added a minimal test suite.


`0.1`_ (2016-10-06)
~~~~~~~~~~~~~~~~~~~

- Initial release!

.. _0.1: https://github.com/matthiask/feincms3-downloads/commit/69a9b98f3111
.. _0.2: https://github.com/matthiask/feincms3-downloads/compare/0.1...0.2
.. _0.3: https://github.com/matthiask/feincms3-downloads/compare/0.2...0.3
.. _0.4: https://github.com/matthiask/feincms3-downloads/compare/0.3...0.4
