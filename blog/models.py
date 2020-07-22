from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    preview = models.TextField()
    url = models.URLField(blank=True)

