from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from django.utils import timezone

# Create your models here.

class EndUser(models.Model):
	user = models.OneToOneField(User, null=True, blank = True, on_delete=models.CASCADE)
	name = models.CharField(max_length = 200, null=True)
	email = models.CharField(max_length = 200, null=True)
	date_created = models.DateField(auto_now_add = True)
	def __str__(self):
		return self.name

class Tag(models.Model):
	CATEGORY = (('My Day', 'My Day'),	
			('Important', 'Important'),
			('Planned', 'Planned'),)
	name = models.CharField(max_length=200, null=True, choices=CATEGORY)
	def __str__(self):
		return self.name

class Task(models.Model):
	user = models.ForeignKey(EndUser, null= True, on_delete = models.SET_NULL)
	title = models.CharField(max_length = 200)
	date_created= DateField(auto_now = True)
	#due_date= DateField(default = timezone.now()+ timezone.timedelta(days=1), null=True) # tomorrow
    #isImportant = BooleanField(default=False) # star amblem at right1
	tags = models.ManyToManyField(Tag, null = True, blank = True)
	def __str__(self):
		return self.title