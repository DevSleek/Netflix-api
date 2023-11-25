from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


class Actor(models.Model):
    GENDER = [
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol')
    ]
    name = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=10)

    def __str__(self):
        return self.name


class Movie(models.Model):
    GENRE = [
        ('Komik', 'Komediya'),
        ('drama', 'Drama'),
        ('detektiv', 'Detektiv'),
        ('jangari', 'Jangari'),
    ]
    name = models.CharField(max_length=50, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    imdb = models.FloatField()
    genre = models.CharField(choices=GENRE, max_length=20)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name


User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField()
    created_date = datetime.now()
    send_time = models.DateTimeField(default=created_date)
