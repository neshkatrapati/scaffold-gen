from django.contrib import admin
from person.models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Job)

admin.site.register(Game)
admin.site.register(GamePlayers)