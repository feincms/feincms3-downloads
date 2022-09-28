import os
import tempfile

from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from feincms3.utils import upload_to

import feincms3_downloads.checks  # noqa
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

    @property
    def basename(self):
        return os.path.basename(self.file.name)

    @property
    def caption_or_basename(self):
        return self.caption or self.basename

    def save(self, *args, **kwargs):
        self.file_size = self.file.size
        super().save(*args, **kwargs)
        if self.show_preview and not self.preview:
            with tempfile.NamedTemporaryFile(
                suffix=os.path.splitext(self.file.name)[1]
            ) as f:
                f.write(self.file.read())
                f.seek(0)
                preview = preview_as_jpeg(f.name)
                if preview:
                    self.preview.save("preview.jpg", ContentFile(preview), save=True)

    save.alters_data = True
