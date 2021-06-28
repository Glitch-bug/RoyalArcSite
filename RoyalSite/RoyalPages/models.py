from django.db import models

class BlogPost(models.Model):
    """An entry in a bloggers web journal"""
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="RoyalSite/images/", null=True, blank=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Returns a string representation of the model"""
        return self.title[:50]

class Gallerys(models.Model):
    pass