import io
import os
from PIL import Image

from django.conf import settings
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


def openimage(path):
    return io.open(os.path.join(settings.MEDIA_ROOT, path), "rb")


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

    def test_simple(self):
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
        self.assertTrue(download.show_preview)
        self.assertFalse(download.preview)

    def test_preview(self):
        client = self.login()
        with openimage("smallliz.tif") as f:
            response = client.post(
                "/admin/testapp/article/add/",
                merge_dicts(
                    zero_management_form_data("testapp_html_set"),
                    zero_management_form_data("testapp_download_set"),
                    {
                        "testapp_download_set-TOTAL_FORMS": 1,
                        "testapp_download_set-0-file": f,
                        "testapp_download_set-0-region": "main",
                        "testapp_download_set-0-ordering": "10",
                        "testapp_download_set-0-show_preview": "1",
                    },
                ),
            )

        self.assertRedirects(response, "/admin/testapp/article/")

        download = Download.objects.get()
        self.assertEqual(download.file_size, 5052)
        self.assertTrue(download.preview.name.endswith(".jpg"))

        image = Image.open(download.preview)
        self.assertEqual(image.size, (160, 160))

    def test_large_image(self):
        client = self.login()
        with openimage("yes.pdf") as f:
            response = client.post(
                "/admin/testapp/article/add/",
                merge_dicts(
                    zero_management_form_data("testapp_html_set"),
                    zero_management_form_data("testapp_download_set"),
                    {
                        "testapp_download_set-TOTAL_FORMS": 1,
                        "testapp_download_set-0-file": f,
                        "testapp_download_set-0-region": "main",
                        "testapp_download_set-0-ordering": "10",
                        "testapp_download_set-0-show_preview": "1",
                    },
                ),
            )

        self.assertRedirects(response, "/admin/testapp/article/")

        download = Download.objects.get()
        self.assertEqual(download.file_size, 15325)
        self.assertTrue(download.preview.name.endswith(".jpg"))

        image = Image.open(download.preview)
        self.assertTrue(image.size[0] <= 310)
