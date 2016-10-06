import io
import subprocess
import tempfile

from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DownloadBase(models.Model):
    file = models.FileField(
        _('file'),
        upload_to='files/%Y/%m',
    )
    caption = models.CharField(
        _('caption'),
        max_length=100,
        blank=True,
    )
    show_preview = models.BooleanField(
        _('show preview'),
        default=True,
    )
    preview = models.ImageField(
        _('preview'),
        blank=True,
        upload_to='preview/%Y/%m',
    )

    class Meta:
        abstract = True
        verbose_name = _('download')
        verbose_name_plural = _('downloads')

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.show_preview and not self.preview:
            with tempfile.TemporaryDirectory() as directory:
                cmd = [
                    'convert', '-geometry', '300', '-quality', '90',
                ]

                if self.file.path.lower().endswith('.pdf'):
                    cmd.extend([
                        '-background', 'white', '-alpha', 'remove'
                    ])

                cmd.extend([
                    '%s[0]' % self.file.path,
                    '%s/pre.jpg' % directory,
                ])

                # print(cmd)
                ret = subprocess.call(cmd, env={
                    'PATH': '/usr/local/bin:/usr/bin:/bin',
                })

                if ret == 0:
                    with io.open('%s/pre.jpg' % directory, 'rb') as f:
                        self.preview.save(
                            'preview.jpg',
                            ContentFile(f.read()),
                            save=True)
    save.alters_data = True
