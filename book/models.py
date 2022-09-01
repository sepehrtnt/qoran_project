from django.db import models


class Verses(models.Model):
    page = models.CharField(max_length=200)
    number_aye = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.topic
