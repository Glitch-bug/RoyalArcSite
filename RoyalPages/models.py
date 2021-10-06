from django.db import models
from cloudinary.models import CloudinaryField
class AboutUs(models.Model):
    """The info about the enterprise to displayed"""
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    text = models.TextField()
    background = CloudinaryField("RoyalArcSite/backgrounds")
    def __str__(self):
        """Returns a string representation of the model"""
        return f"{self.title[:50]} ({self.order})"
        
class BlogPost(models.Model):
    """An entry in a bloggers web journal"""
    title = models.CharField(max_length=200)
    cover = CloudinaryField("RoyalArcSite/covers")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        """Returns a string representation of the model"""
        return self.title[:50]

class Catergory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    """Pictures mooore pictures"""
    title = models.CharField(max_length=200, null=True, blank=True)
    image = CloudinaryField("RoyalArcSite/gallery")