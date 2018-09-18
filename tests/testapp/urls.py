from django.conf.urls import include, url
from django.contrib import admin

from testapp import views


articles_urlpatterns = (
    [url(r"^(?P<pk>[0-9]+)/$", views.article_detail, name="article")],
    "articles",
)


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"", include(articles_urlpatterns)),
]
