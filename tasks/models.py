from django.db.models import Model, CharField, BooleanField
from django.db.models.fields import DateField
from django.utils import timezone

# Create your models here.
class Task(Model):
    title = CharField(max_length = 200)
    isCompleted = BooleanField(default=False)
    date_created= DateField(auto_now = True)
    #due_date= DateField(default = timezone.now()+ timezone.timedelta(days=1), null=True) # tomorrow
    #isImportant = BooleanField(default=False) # star amblem at right
    
    def __str__(self):
        return self.title