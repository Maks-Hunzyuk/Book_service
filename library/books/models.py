from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    books = models.ManyToManyField('Book', blank=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    year_published = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books',
                               on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

    def author(self) -> Author:
        return Author.objects.get_or_create(
            first_name=self.title.split()[0],
            last_name=self.title.rsplit(',')[0],
        )[1]
