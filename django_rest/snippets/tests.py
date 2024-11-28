from django.test import TestCase
from .models import Snippet
from django.contrib.auth.models import User

class SnippetTestCase(TestCase):

    def setUp(self):
        user = User.objects.create()
        Snippet.objects.create(code="print(123)", owner=user)
        Snippet.objects.create(code="print(456)", owner=user)

    def test_objects_exist(self):
        snippet1 = Snippet.objects.get(code="print(123)")
        self.assertEqual(snippet1.code, "print(123)")
