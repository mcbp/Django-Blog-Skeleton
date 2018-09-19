from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    thumbnail = models.ImageField(default='default_thumbnail.png', blank=True)

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:100] + '...'
