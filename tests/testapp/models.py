from content_editor.models import Region, create_plugin_base
from django.db import models
from django.utils.translation import gettext_lazy as _
from feincms3 import plugins

from feincms3_downloads.plugins import DownloadBase


class Article(models.Model):
    regions = [Region(key="main", title=_("main"))]


ArticlePlugin = create_plugin_base(Article)


class HTML(plugins.html.HTML, ArticlePlugin):
    pass


class Download(DownloadBase, ArticlePlugin):
    pass
