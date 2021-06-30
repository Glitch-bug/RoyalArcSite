from django.db import models

class AboutUs(models.Model):
    """The info about the enterprise to displayed"""
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    text = models.TextField()
    def __st__(self):
        """Returns a string representation of the model"""
        return self.title[:50]
        
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
    """Pictures mooore pictures"""
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="RoyalSite/images/gallery", default="RoyalSite/images/gallery/x.png")
    def __str__(self):
        """Returns a string representation of the model"""
        return self.title[:50]
