from django.core.management.base import BaseCommand, CommandError
from django.db import models
import os,inspect


class Command(BaseCommand):
    args = "<appname modelname fieldname:fieldtype:fieldargs ..>"
    help = "Generates ROR style scaffolds"
    f_map = {
           "text" : "models.CharField",
           "int" : "models.IntegerField",
           "date" : "models.DateTimeField",
           "f" : "models.ForeignKey"
        }

    def handle(self, *args, **options):
        if len(args) < 2:
            self.stderr.write("Usage, <appname modelname fieldname:fieldtype:fieldargs ..>")
            return None

        app_name = args[0] 
        if (not os.path.exists(app_name)) or (not os.path.isdir(app_name)):
            self.stderr.write("No such app, {app_name} found".format(**locals()))
            return None
        if (not os.path.exists(app_name+"/models.py")):
             self.stderr.write("Models.py not found at {app_name}/".format(**locals()))


        class_name = args[1]
        if ':' in class_name:
            self.stderr.write("Invalid Class name, {class_name}".format(**locals()))
            return None

        class_rep = app_name + ".models." + class_name
#        print models.get_models()
        if class_rep in [model.__module__ + "." + model.__name__ for model in models.get_models()]:
            self.stderr.write("Class : {class_name} already exists".format(**locals()))
            return None

        fields = {}
        for arg in args[2:]:
            if ':' not in arg:
                self.stderr.write("Invalid field format, {arg}".format(**locals()))
                return None
            arg = arg.split(":")
            if arg[1] not in self.f_map.keys():
                self.stderr.write("Invalid field type, {type}".format(type=arg[1]))
                return None
            if arg[1] == "text":              
                fields[arg[0]] = self.f_map[arg[1]]+"(max_length=255)"
            elif arg[1] != "f":
                fields[arg[0]] = self.f_map[arg[1]]+"()"
            else: 
                if len(arg) < 3:
                    self.stderr.write("ForeignKey requires modelname, Wrong format: {format}".format(format=":".join(arg)))
                    return None
                fields[arg[0]] = self.f_map[arg[1]]+"("+arg[2]+")"
                
        #import pprint 
        #pprint.pprint(fields)
        
        with open(app_name+"/models.py","a") as f:
           to_write = "class {class_name}(models.Model):\n".format(**locals())
           self.stdout.write("Generating class {class_name}".format(**locals()))
           if len(fields) < 1: 
               to_write += "\tpass"
           for field in fields:
               self.stdout.write("Generating field {fname} as {ftype}".format(fname=field,ftype=fields[field]))
               to_write += "\t{fname} = {ftype}\n".format(fname=field,ftype=fields[field])
          
           f.write(to_write)
           self.stdout.write("Done !")
           

            
