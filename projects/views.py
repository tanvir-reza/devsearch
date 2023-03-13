from django.shortcuts import render,redirect
from projects.models import User,Project
from .forms import ProjectForm,Reviews
from django.db.models.query import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    users = User.objects.all()
    data = {"users":users}
    return render(request,'index.html',context=data)

def projects(request):
    project_search = ""
    if request.GET.get('project-search'):
        project_search = request.GET.get('project-search')
        projects = Project.objects.filter(title__icontains=project_search)
    else:
        projects = Project.objects.all()
    # tag = projects.tags.all()
    print(projects)
    data = {"projects":projects}
    return render(request,'projects.html',context=data)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tag.all()
    form = Reviews()
    
    if request.method == 'POST':
        form = Reviews(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        try:
            review.save()
            projectObj.getVoteCount()
            messages.success(request,"Review Send  Successfully !!!")
            return redirect('project', pk=projectObj.id)
        except:
            messages.success(request,"Only One Review for Any User")
            return redirect('project', pk=projectObj.id)
    
    return render(request, 'project.html',{'project':projectObj,'tags':tags,'form':form})

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    profile = request.user.profile
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            
            return redirect('projects')

    data = {'form':form}
    return render(request,'create-project.html',data)


@login_required(login_url='login')
def updateProject(request,pk):
    user = request.user.profile
    project = user.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            messages.success(request,"Project Update Successfully !!!")
            return redirect('projects')

    data = {'form':form}
    return render(request,'update-project.html',data)

@login_required(login_url='login')
def deleteProject(request,pk):
    user = request.user.profile
    project = user.project_set.get(id=pk)
    if request.method == 'GET':
        project.delete()
        messages.success(request,"Project Delete Successfully !!!")
        return redirect('editAccount')

    return redirect('editAccount')

