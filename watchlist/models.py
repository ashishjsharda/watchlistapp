from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title