from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userImage(models.Model):
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to='images/')

    def __str__(self):
        return self.user.username

class FilteredImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='filters', on_delete = models.CASCADE)
    centroid = models.ExpressionList

    def __str__(self):
        return self.base_image.user.username