from django.test import TestCase
from testproj.testapp.models import Book


class BookTests(TestCase):
    def test_book(self):
        Book.objects.create(title="Foo")
