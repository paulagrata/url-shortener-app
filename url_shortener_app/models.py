from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField(null=True)  # Allow null values for the original URL
    short_code = models.CharField(max_length=50, unique=True)  # Field to store shortened code

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
