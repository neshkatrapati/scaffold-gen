from django.db import models

class Person(models.Model):
	dob = models.DateTimeField()
	age = models.IntegerField()
	name = models.CharField(max_length=255)
	height = models.IntegerField()

class Job(models.Model):
	duration = models.DateTimeField()
	person = models.ForeignKey(Person)
	name = models.CharField(max_length=255)

class Game(models.Model):
	country_of_origin = models.CharField(max_length=255)
	number_of_players = models.IntegerField()
	name = models.CharField(max_length=255)

class GamePlayers(models.Model):
	person = models.ForeignKey(Person)
	game = models.ForeignKey(Game)
	nth_favourite = models.IntegerField()
	
	class Meta:
		verbose_name_plural = "Game Players"
