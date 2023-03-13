from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Skill,Message

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','phone','username','location','short_intro','occupation','bio','profile_img','github_link','linkedin_link','facebook_link']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'short_intro' : forms.TextInput(attrs={'class':'form-control'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control'}),
            'bio' : forms.TextInput(attrs={'class':'form-control'}),
            'profile_img' : forms.FileInput(attrs={'class':'form-control'}),
            'github_link' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_link' : forms.TextInput(attrs={'class':'form-control'}),
            'facebook_link' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']
        exclude = []
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Skill Name'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Skill Description'}),
        }

        # def __init__(self,*args,**kwargs):
        #     super(SkillForm, self).__init__(*args,**kwargs)

        #     for name , field in self.fields.items():
        #         field.widget.attrs.update({'class':'form-control'})
