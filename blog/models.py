from django.db import models


class BlogsContent(models.Model):
    blogs_title = models.CharField(max_length=100)
    blogs_date = models.DateField(verbose_name="Date")
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)
