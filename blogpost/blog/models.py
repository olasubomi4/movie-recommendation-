from __future__ import unicode_literals

from django.db import models

# Create your models here.
class movies2(models.Model):
	keywords = models.CharField(max_length=100)
	cast = models.CharField(max_length=100)
	genres = models.CharField(max_length=100)
	director = models.CharField(max_length=100)

class movies(models.Model):
	movie_id = models.IntegerField(default=0)
	imdb_id = models.IntegerField(default=0)
	movie_name = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	vectors = models.CharField(max_length=20)

class movies6(models.Model):
	index = models.IntegerField(default=0)
	budget= models.IntegerField(default=0)
	genres= models.CharField(max_length=100)
	homepage = models.CharField(max_length=100)
	id = models.IntegerField(default=0 ,primary_key=True)
	keywords = models.CharField(max_length=100)
	original_language = models.CharField(max_length=100)
	original_title = models.CharField(max_length=100)
	overview = models.CharField(max_length=100)
	popularity = models.IntegerField(default=0)
	production_companies = models.CharField(max_length=100)
	production_countries= models.CharField(max_length=100)
	release_date = models.CharField(max_length=100)
	revenue = models.IntegerField(default=0)
	runtime = models.IntegerField(default=0)
	spoken_languages = models.CharField(max_length=100)
	status = models.CharField(max_length=100)
	tagline = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	vote_average = models.IntegerField(default=0)
	vote_count = models.IntegerField(default=0)
	cast = models.CharField(max_length=256)
	crew = models.CharField(max_length=256)
	director = models.CharField(max_length=256)

class meansize(models.Model):
	movie_id = models.IntegerField(default=0)
	size = models.FloatField(default=0.0)
	mean = models.FloatField(default=0.0)

class links(models.Model):
	movie_id = models.IntegerField(default=0)
	url = models.CharField(max_length=300)




#class Post(models.Model):
    #title = models.TextField()
    #cover = models.ImageField(upload_to='images/')

   # def __str__(self):
        #return self.title