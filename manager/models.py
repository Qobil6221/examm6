from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
