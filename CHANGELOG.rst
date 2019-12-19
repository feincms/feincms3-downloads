==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

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
.. _Next version: https://github.com/matthiask/feincms3-downloads/compare/0.2...master
