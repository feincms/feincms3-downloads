from django.contrib import admin
from django.urls import include, path, re_path

from testapp import views


articles_urlpatterns = (
    [path("<int:pk>/", views.article_detail, name="article")],
    "articles",
)


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("", include(articles_urlpatterns)),
]
