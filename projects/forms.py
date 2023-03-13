from django.forms import ModelForm
from .models import Project,Review
from django import forms



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','project_img','demo_link','project_link','tag']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Project Title'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Project Description'}),
            'project_img' : forms.FileInput(attrs={'class':'form-control'}),
            'demo_link' : forms.URLInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'project_link' : forms.URLInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'project_link' : forms.URLInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
        }

class Reviews(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        widgets = {
            'value' : forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Project Description'})

        }