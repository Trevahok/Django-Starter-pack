from django.db import models
from django.contrib.auth.models import  User
from django.db.models.signals import  post_save
from django.urls import  reverse_lazy

# Create your models here.

class Profile(models.Model):
    ''' A model for user profile page that stores all the specifics. '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    height = models.FloatField(null=True,help_text='Height in m.')
    weight = models.FloatField(null=True, help_text='Weight in Kgs.')
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return self.user.username
    @property
    def bmi(self):
        return  self.weight /( self.height)**2
    
    def get_absolute_url(self):
        return reverse_lazy('profile_update') 

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile =Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
