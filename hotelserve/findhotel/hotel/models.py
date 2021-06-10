from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=250)
    long_description = models.TextField(max_length=2000, null=True)
    HOTEL_STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    stars = models.TextField(max_length=1, default=5, choices=HOTEL_STARS, null=True)
    pictures = models.ImageField(upload_to="images", default="images/default.jpg")
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)