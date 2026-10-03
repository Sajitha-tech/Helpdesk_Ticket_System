from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   phone=models.CharField(max_length=15,unique=True)

class Ticket(models.Model):
   
   title=models.CharField(max_length=150,blank=False)
   description=models.TextField()
   priority_choice=[('low','low'),('medium','medium'),('high','high')]

   priority=models.CharField(max_length=20,choices=priority_choice,default='low')

   status_choice=[('open','open'),('in_progress','in_progress'),('resolved','resolved')]

   status=models.CharField(max_length=20,choices=status_choice,default='open')

   created_by=models.ForeignKey(User,on_delete=models.CASCADE)

   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.created_by.username
   

