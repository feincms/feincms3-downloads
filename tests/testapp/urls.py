from django.contrib import admin
from django.urls import include, re_path
from testapp import views

articles_urlpatterns = (
    [re_path(r"^(?P<pk>[0-9]+)/$", views.article_detail, name="article")],
    "articles",
)


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"", include(articles_urlpatterns)),
]
