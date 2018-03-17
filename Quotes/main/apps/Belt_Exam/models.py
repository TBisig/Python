from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def Regvalidator(self, postData):
		errors = {}
		if len(postData['Rname']) < 3:
			errors["name"] = "Name should be more than 3 characters"
		if len(postData['Ruser']) < 3:
			errors["name"] = "Username should be more than 3 characters"
		if len(User.objects.filter(username=postData['Ruser'])) > 0:
			errors["samename"] = "Username taken"
		if len(postData['Remail']) < 5:
			errors["name"] = "Email should be more than 5 characters"
		if len(User.objects.filter(email=postData['Remail'])) > 0:
			errors["sameemail"] = "You are already a member"
		if len(postData['Rpass']) < 8:
			errors["password"] = "Password should be more than 8 characters"
		if postData['Rpass'] != postData['RpassC']:
			errors['pwd match'] = 'Passwords do not match'
		if len(errors) == 0:
			errors['Registered!'] = 'Registered!'
			hash1 = bcrypt.hashpw(postData['Rpass'].encode(), bcrypt.gensalt())
		if len(postData['birthdate']):
			User.objects.create(name=postData['Rname'], password=hash1,username=postData['Ruser'], email=postData['Remail'], birthdate=postData['birthdate'])
			print 'hi'
		return errors
	def Logvalidator(self, postData):
		errors = {}
		if len(User.objects.filter(email=postData['Lemail'])) == 0:
			errors['namefail'] = 'incorrect email'
		else:
			P = User.objects.get(email=postData['Lemail']).password
			Z = postData['Lpass']
			if not bcrypt.checkpw(Z.encode(), P.encode()):
				errors['PassFail'] = 'incorrect Password'
		return errors
class User(models.Model):
	name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	birthdate = models.DateField()
	favorites = models.ManyToManyField("Quote", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return "name:{}, username:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.alias, self.email, self.password, self.created_at, self.updated_at)

class QuoteManager(models.Manager):
	def validateQuote(self, postData):
		is_valid = True
		errors = []
		if len(postData.get('content')) < 10:
			is_valid = False
			errors.append('Message must be more than 10 characters')
		return (is_valid, errors)
class Quote(models.Model):
	content = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'authored_quotes')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = QuoteManager()

	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)