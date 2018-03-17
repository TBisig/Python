from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def Regvalidator(self, postData):
        errors = {}
        if len(postData['Rname']) < 3:
            errors["name"] = "Name should be more than 3 characters"
        if len(postData['Ruser']) < 3:
            errors["name"] = "Username should be more than 3 characters"
        if len(User.objects.filter(username=postData['Ruser'])) > 0:
            errors["samename"] = "Username taken"
        if len(postData['Rpass']) < 8:
            errors["password"] = "Password should be more than 8 characters"
        if postData['Rpass'] != postData['RpassC']:
        	errors['pwd match'] = 'Passwords do not match'
        if len(errors) == 0:
        	errors['Registered!'] = 'Registered!'
        	hash1 = bcrypt.hashpw(postData['Rpass'].encode(), bcrypt.gensalt())
        	User.objects.create(name=postData['Rname'], password=hash1,username=postData['Ruser'])
        	print 'hi'
        return errors
    def Logvalidator(self, postData):
    	errors = {}
    	if len(User.objects.filter(name=postData['Lname'])) == 0:
    		errors['namefail'] = 'incorrect name'
    	else:
    		P = User.objects.get(name=postData['Lname']).password
    		Z = postData['Lpass']
    		if not bcrypt.checkpw(Z.encode(), P.encode()):
    			errors['PassFail'] = 'incorrect Password'
    	return errors
class TripManager(models.Manager):
    def TripValidator(self, postData,plannedby):
        destination = postData['Adest']
        description = postData['Adesc']
        startdate = postData['Sdate']
        enddate = postData['Edate']
        errors = {}
        if startdate > enddate:
            errors['Learn dates'] = 'Start date is before end date'
        else:
            u = Vacation.objects.create(destination=destination,description=description,startdate=startdate,enddate=enddate ,creator_id=plannedby)
            this_user = User.objects.get(id=plannedby)
            u.users.add(this_user)
            u.save()
        return errors
class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = UserManager()
class Vacation(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    creator = models.ForeignKey(User, related_name='Vacations')
    users = models.ManyToManyField(User)
    objects = TripManager()