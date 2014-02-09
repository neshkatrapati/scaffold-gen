Django Scaffold Generator
=========================

Introduction
------------
This module generates model and admin code given some description. 

Installation
------------
Download this, put it in your project and, add 'scaffold_gen' in INSTALLED_APPS of settings.py. Then do, 'python manage.py syncdb'

Usage
-----
To generate models, first do,
   	    
	    $ python manage.py startapp <appname>
	    $ python manage.py startapp person

Then,
	
	    $ python manage.py modelgen <appname> <modelname> [<field_name>:<field_type>:<field_params> ..]
	    $ python manage.py modelgen person Person name:text age:int dob:date
	    $ python manage.py modelgen person Job name:text duration:date person:f:Person

This generates,
	
```python 
class Person(models.Model):
	dob = models.DateTimeField()
	age = models.IntegerField()
	name = models.CharField(max_length=255)
	height = models.IntegerField()

class Job(models.Model):
	duration = models.DateTimeField()
	person = models.ForeignKey(Person)
	name = models.CharField(max_length=255)  
```

	    
For generating admin, 
    
	    $ python manage.py scaffoldgen --admin <fully_qualified_model_name>
	    $ python manage.py scaffoldgen --admin person.models.Person
	    

This generates, 
        
```python
	    
admin.site.register(Person)
```


Note :: You must have the line "from person.models import *" at the top of person/admin.py. 
This program will not add it
Note :: This program will not check for duplicate registration
	    
	    
	     



