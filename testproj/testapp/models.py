from django.db import models


class Author(models.Model):
    pass


class Book(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        unique_together = [["title", "author"]]
