from django.db import models


class Index(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name