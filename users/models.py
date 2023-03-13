from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    occupation = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    profile_img = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/profile.jpg')
    github_link = models.URLField(max_length=200,blank=True)
    linkedin_link = models.URLField(max_length=200,blank=True)
    facebook_link = models.URLField(max_length=200,blank=True)
     
    def __str__(self):
        return self.first_name
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name="messages")
    name = models.CharField(max_length=200,null=True,blank=True)
    is_read = models.BooleanField(default=False,null=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField(max_length=200,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.subject 
    
    class Meta:
        ordering = ['is_read', '-created']




