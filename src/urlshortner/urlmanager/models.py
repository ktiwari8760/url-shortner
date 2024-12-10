from django.db import models

# Create your models here.
class UrlModel(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    last_clicked = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.url