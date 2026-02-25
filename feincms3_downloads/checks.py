import os
import shutil

from django.core.checks import Error, register


@register
def check_binaries(app_configs, **kwargs):
    path = os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin")

    errors = []
    if not shutil.which("convert", path=path):
        errors.append(
            Error(
                'The "convert" binary could not be found',
                hint="Try installing ImageMagick.",
                id="feincms3_downloads.E001",
            )
        )
    if not shutil.which("pdftocairo", path=path):
        errors.append(
            Error(
                'The "pdftocairo" binary could not be found',
                hint="Try installing poppler-utils.",
                id="feincms3_downloads.E001",
            )
        )
    return errors
