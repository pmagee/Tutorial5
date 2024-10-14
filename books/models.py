from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

