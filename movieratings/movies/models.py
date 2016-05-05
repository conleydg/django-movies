from django.db import models

# Create your models here.
class Rater(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    age = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, default ='')
    occupation = models.CharField(max_length=255)


class Movies(models.Model):
    movie_id = models.CharField(max_length=255, primary_key=True)
    movie_title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)


class Rating(models.Model):
    user_id = models.CharField(max_length=255)
    movie_id = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    # rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    # movies = models.ForeignKey(Movies, on_delete=models.CASCADE)
