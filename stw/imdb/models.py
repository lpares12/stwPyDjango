from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
	name = models.CharField(max_length=75)
	description = models.CharField(max_length=300)
	cover_img = models.CharField(max_length=300)
	def __str__(self):
		return self.name + ':' + self.description

# CREATE TABLE "imdb_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(75) NOT NULL, "description" varchar(300) NOT NULL, "cover_img" varchar(300) NOT NULL);

class Comment(models.Model):
	movie = models.ForeignKey(Movie)
	name = models.CharField(max_length=30)
	text = models.CharField(max_length=200)
	def __str__(self):
		return self.name + ':' + self.text
