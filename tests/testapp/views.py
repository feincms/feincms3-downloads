from django.shortcuts import get_object_or_404, render

from feincms3 import plugins
from feincms3.renderer import TemplatePluginRenderer

from .models import Article, HTML, Download


renderer = TemplatePluginRenderer()
renderer.register_string_renderer(HTML, plugins.html.render_html)
renderer.register_template_renderer(Download, "plugins/download.html")


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(
        request,
        "article.html",
        {"article": article, "regions": renderer.regions(article)},
    )
