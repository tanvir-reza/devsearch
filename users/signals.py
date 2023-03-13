from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender,instance,created, **kwargs):
    print("profile Trigger")
    if(created):
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            first_name = user.first_name
        )


def updateUser(sender,instance,created,**kwargs):
    profile = instance
    print("update Trigger")
    print(profile)
    user = profile.user
    if created == False:
        user.username = profile.username
        user.first_name = profile.first_name
        user.email = profile.email
        user.short_intro = profile.short_intro
        user.bio = profile.bio
        user.save()



post_save.connect(updateUser,sender=Profile)
post_save.connect(createProfile,sender=User)