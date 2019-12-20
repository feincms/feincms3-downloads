import shutil

from django.core.checks import Error, register


@register
def check_binaries(app_configs, **kwargs):
    errors = []
    if not shutil.which("convert", path="/usr/local/bin:/usr/bin:/bin"):
        errors.append(
            Error(
                'The "convert" binary could not be found',
                hint="Try installing ImageMagick.",
                id="feincms3_downloads.E001",
            )
        )
    if not shutil.which("pdftocairo", path="/usr/local/bin:/usr/bin:/bin"):
        errors.append(
            Error(
                'The "pdftocairo" binary could not be found',
                hint="Try installing poppler-utils.",
                id="feincms3_downloads.E001",
            )
        )
    return errors
