from content_editor.admin import ContentEditor, ContentEditorInline
from django.contrib import admin
from feincms3 import plugins

from testapp import models


@admin.register(models.Article)
class ArticleAdmin(ContentEditor):
    inlines = [
        plugins.html.HTMLInline.create(model=models.HTML),
        ContentEditorInline.create(model=models.Download),
    ]
