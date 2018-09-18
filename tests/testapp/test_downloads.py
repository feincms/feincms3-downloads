from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.test import Client, TestCase
from django.utils.translation import deactivate_all

from .models import Article, HTML, Download


def zero_management_form_data(prefix):
    return {
        "%s-TOTAL_FORMS" % prefix: 0,
        "%s-INITIAL_FORMS" % prefix: 0,
        "%s-MIN_NUM_FORMS" % prefix: 0,
        "%s-MAX_NUM_FORMS" % prefix: 1000,
    }


def merge_dicts(*dicts):
    res = {}
    for d in dicts:
        res.update(d)
    return res


class Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser("admin", "admin@test.ch", "blabla")
        deactivate_all()

    def login(self):
        client = Client()
        client.force_login(self.user)
        return client

    def test_modules(self):
        """Admin modules are present, necessary JS too"""

        client = self.login()

        response = client.get("/admin/")
        self.assertContains(
            response, '<a href="/admin/testapp/article/">Articles</a>', 1
        )

    def test_view(self):
        article = Article.objects.create()
        HTML.objects.create(
            parent=article, ordering=1, region="main", html="<b>Hello</b>"
        )
        download = Download(parent=article, ordering=2, region="main")
        download.file.save("world.txt", ContentFile("World"))

        response = self.client.get("/{}/".format(article.pk))
        self.assertContains(response, "<b>Hello</b>")
        self.assertContains(response, 'class="download button"')

        self.assertEqual(download.file_size, 5)
