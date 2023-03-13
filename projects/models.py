from django.db import models
import uuid
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

from django.db.models.signals import post_save


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    demo_link = models.URLField(max_length=200,blank=True)
    project_link = models.URLField(max_length=200,blank=True)
    project_img = models.ImageField(null=True,blank=True,default='default.jpg')
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True, default=Profile)
    total_vote = models.IntegerField(default=0,null=True,blank=True)
    vote_ration = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag',blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes/totalVotes) *100

        self.total_vote = totalVotes
        self.total_ratio = ratio
        self.total_vote = totalVotes
        self.save()


class Review(models.Model):
    VOTE_TYPE=(
        ('up',"Up Vote"),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    class Meta:
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.name



def profileUpdate(sender,instance,created, **kwargs):
    print("Profile Updated !!")


post_save.connect(profileUpdate,sender=Project)

