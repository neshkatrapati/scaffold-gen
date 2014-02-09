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
