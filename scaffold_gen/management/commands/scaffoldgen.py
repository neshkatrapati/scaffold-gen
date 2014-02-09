from django.core.management.base import BaseCommand, CommandError
from django.db import models
import os,inspect
from optparse import make_option


class Command(BaseCommand):
    args = "<model_full_qualified_name>"
    help = "Generates ROR style scaffolds"
    option_list = BaseCommand.option_list + (
        make_option('--admin',
            action='store_true',
            dest='admin',
            default=False,
            help='Generate admin.py'),
        )

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write("Usage, <model_full_qualified_name>")
            return None
        model_name = args[0]
        model_p = args[0].split(".")
        app_name = model_p[0]
        model_list = [model.__module__ + "." + model.__name__ for model in models.get_models()]
        if model_name not in model_list:
            self.stderr.write("No such model : {model_name} found. Have you registered your app in settings.py ?".format(**locals()))
            return None

        if options["admin"]:
            self.stdout.write("Note :: You must have the line \"{line}\" at the top of {filename}. \nThis program will not add it".format(line = "from "+ model_p[0] +".models import *", filename=model_p[0] + "/admin.py" ))
            self.stdout.write("Note :: This program will not check for duplicate registration")
            if (not os.path.exists(app_name + "/admin.py")):
                self.stdout.write("{app_name}/admin.py not found, I am creating it.".format(**locals()))
                a_file = open(app_name + "/admin.py","w") 
                prepend =  "from django.contrib import admin"
                prepend += "from {mname} import *".format(mname = ".".join(model_p[1:]))
                a_file.write(prepend)
                
            else: 
                with open(app_name + "/admin.py","a") as f: 
                    prefix = ".".join(model_p[:-1])
                    f.write("\nadmin.site.register({mname})".format(mname = model_p[-1]))
                    self.stdout.write("Done !!")

