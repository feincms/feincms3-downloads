from django.contrib import admin

from content_editor.admin import ContentEditor, ContentEditorInline
from feincms3 import plugins

from . import models


@admin.register(models.Article)
class ArticleAdmin(ContentEditor):
    inlines = [
        plugins.html.HTMLInline.create(model=models.HTML),
        ContentEditorInline.create(model=models.Download),
    ]
