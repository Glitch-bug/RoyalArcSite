from django.db import models

class AboutUs(models.Model):
    """The info about the enterprise to displayed"""
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    text = models.TextField()
    background = models.ImageField(upload_to="media/", default="RoyalSite/static/RoyalSite/images/gallery/x.png")
    def __str__(self):
        """Returns a string representation of the model"""
        return f"{self.title[:50]} ({self.order})"
        
class BlogPost(models.Model):
    """An entry in a bloggers web journal"""
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="media/", null=True, blank=True)
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
    image = models.ImageField(upload_to="media/", default="RoyalSite/static/RoyalSite/images/gallery/x.png")

