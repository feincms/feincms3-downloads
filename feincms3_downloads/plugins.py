from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _

from .previews import preview_as_jpeg


class DownloadBase(models.Model):
    file = models.FileField(_("file"), upload_to="files/%Y/%m")
    file_size = models.IntegerField(_("file size"), editable=False)
    caption = models.CharField(_("caption"), max_length=100, blank=True)
    show_preview = models.BooleanField(_("show preview"), default=True)
    preview = models.ImageField(_("preview"), blank=True, upload_to="preview/%Y/%m")

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
            preview = preview_as_jpeg(self.file.path)
            if preview:
                self.preview.save("preview.jpg", ContentFile(preview), save=True)

    save.alters_data = True
