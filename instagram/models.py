from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='video/')
    description = models.TextField()
    video_likes = models.IntegerField(default=0)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    create_at = models.DateField()

    def __str__(self):
        return f'{self.id} - {self.subcategory.name}'


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Like(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    liked_video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.liked_video.subcategory.name}"

