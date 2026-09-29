# Agent Instructions for feincms3-downloads

This document provides guidance for AI coding agents working on the feincms3-downloads codebase.

## Repository Overview

feincms3-downloads provides an abstract download plugin for feincms3 / django-content-editor. It stores the file size and automatically generates JPEG previews of uploaded files using external binaries.

**Key directories:**
- `feincms3_downloads/` - Main package code
- `tests/testapp/` - Test application and test suite

**Core modules:**
- `plugins.py` - `DownloadBase` abstract model and `generate_preview()`
- `previews.py` - `preview_as_jpeg()`, shells out to `pdftocairo` (PDFs) or ImageMagick's `convert` (everything else)
- `checks.py` - Django system checks for the required binaries
- `templates/plugins/download.html` - Default rendering template

## Development Workflow

### Requirements

The external binaries `convert` (ImageMagick) and `pdftocairo` (poppler-utils) must be installed; tests generate real previews.

### Testing Requirements

**Run tests through tox:**
```bash
tox -e py313-dj52  # Run specific Python/Django version
tox -l             # List available test environments
```

**Test suite structure:**
- `tests/testapp/test_downloads.py` - Model, preview generation and admin tests
- Test media (`smallliz.tif`, `yes.pdf`) lives in `tests/testapp/media/`

**Important testing practices:**
- Write tests for new functionality in `test_downloads.py`
- Place imports at the top of test files, not inside test methods
- Tests must pass before changes are considered complete

### Code Style

- Follow existing code style (project uses pre-commit hooks with ruff and biome)
- Run `prek` to execute pre-commit hooks before committing
- Keep code minimal and focused - avoid over-engineering
- Prefer editing existing files over creating new ones
- Don't add comments, docstrings, or type annotations to unchanged code
- Only add error handling where truly necessary (at boundaries)
- Record user-visible changes in `CHANGELOG.rst` under "Next version"

## Architecture Considerations

**DownloadBase:**
- Abstract model; projects combine it with their own plugin base (see `tests/testapp/models.py`)
- `save()` stores `file_size`, then generates a preview after the first save if `show_preview` is set and no preview exists yet, and saves again with `update_fields=["preview"]`
- `basename` and `caption_or_basename` are convenience properties for templates

**Preview generation:**
- The source file is copied to a temporary file (keeping its extension) because the external binaries need a real path; storage backends may not be local
- `preview_as_jpeg()` returns `None` when the binary fails, in which case no preview is stored
- The subprocess environment only contains `PATH`

### System Checks

- `feincms3_downloads.E001` - `convert` binary not found
- `feincms3_downloads.E002` - `pdftocairo` binary not found

## Git and Version Control

- Repository is at `github.com/matthiask/feincms3-downloads`
- Don't commit unless explicitly requested
- Commit feature by feature, not everything at once. Each commit should stand
  on its own: ship a change together with the tests covering it, so that the
  test suite passes at every commit.
- Write short commit messages: one imperative summary line, matching the
  existing log (no `feat:`/`fix:` prefixes). The message doesn't have to repeat
  what the diff already says; only add a body when the *why* isn't obvious.
- Never add attribution to commits: no `Co-Authored-By` trailers, no
  "Generated with ..." lines, no other agent or tool attribution.
- Never use `--no-verify` or skip hooks
- Stage specific files by name (avoid `git add -A`)
- Watch for sensitive files (.env, credentials) before staging

## File Organization

**Don't create unnecessary files:**
- No new markdown/documentation files without explicit request
- Don't create helper utilities for one-time operations
- Don't add configuration for hypothetical future needs

**Translations:**
- Locale files in `feincms3_downloads/locale/`
- Use Django's translation functions (`gettext`, `gettext_lazy`)

## References

- Django documentation: https://docs.djangoproject.com/
- feincms3: https://feincms3.readthedocs.io/
- django-content-editor: https://django-content-editor.readthedocs.io/
