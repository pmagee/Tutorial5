from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

