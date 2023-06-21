import os
import tempfile

from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from feincms3.utils import upload_to

import feincms3_downloads.checks  # noqa: F401
from feincms3_downloads.previews import preview_as_jpeg


class DownloadBase(models.Model):
    file = models.FileField(_("file"), upload_to=upload_to)
    file_size = models.IntegerField(_("file size"), editable=False)
    caption = models.CharField(_("caption"), max_length=100, blank=True)
    show_preview = models.BooleanField(_("show preview"), default=True)
    preview = models.ImageField(_("preview"), blank=True, upload_to=upload_to)

    class Meta:
        abstract = True
        verbose_name = _("download")
        verbose_name_plural = _("downloads")

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        self.file_size = self.file.size
        super().save(*args, **kwargs)
        if self.show_preview and not self.preview:
            generate_preview(source=self.file, preview=self.preview)

    save.alters_data = True

    @property
    def basename(self):
        return os.path.basename(self.file.name)

    @property
    def caption_or_basename(self):
        return self.caption or self.basename


def generate_preview(*, source, preview, save=True):
    with tempfile.NamedTemporaryFile(suffix=os.path.splitext(source.name)[1]) as f:
        f.write(source.read())
        f.seek(0)
        if p := preview_as_jpeg(f.name):
            preview.save("preview.jpg", ContentFile(p), save=save)
