from django.db import models
import datetime
import time

class Video(models.Model):
    title_text = models.CharField(max_length=250)
    plot = models.TextField()
    rating = models.CharField(max_length=55)
    poster = models.TextField()
    available_imax = models.BooleanField(default=False)
    available_3d = models.BooleanField(default=False)
    release_date = models.DateField()
    pilot = models.CharField(max_length=50)

    class Meta:
       abstract = True

class Movie(Video):
    duration = models.CharField(max_length=100)
    trailer_youtube_url = models.TextField()
    budget = models.TextField(default=" ")
    trivia = models.TextField(default=" ")
    goofs = models.TextField(default=" ")

    def __unicode__(self):
        return self.title_text

class Show(Video):
    seasons = models.IntegerField(default=1)
    network = models.CharField(max_length=250)

    def __unicode__(self):
        return self.title_text

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)

    class Meta:
        abstract = True

class MoviePerson(Person):
    movie = models.ForeignKey(Movie,null=True)

    def __unicode__(self):
        return self.first_name

class ShowPerson(Person):
    show = models.ForeignKey(Show,null=True)

    def __unicode__(self):
        return self.first_name





