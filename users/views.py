from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from .models import Profile,Message
from .forms import CustomUserCreateForm,ProfileForm,SkillForm,MessageForm
from django.contrib.auth.models import User

def profiles(request):
    s_q = ""
    if request.GET.get('s_q'):
        s_q = request.GET.get('s_q')
        users = Profile.objects.filter(first_name__icontains=s_q)
        print(users)
    else:
        users = Profile.objects.all()
    context = {'users':users}
    return render(request,'users/profiles.html',context=context)


@login_required(login_url='login')
def editAccount(request):
    p = Profile.objects.get(username=request.user.username)
    form = ProfileForm(instance=p)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"Profile Update Successfully !!!")
            return redirect('user')
        else:
            messages.error(request,"Something Wrong !!!")
            return redirect('editAccount')
    context = {"form":form}
    return render(request,'users/profileform.html',context=context)


def signupUser(request):
    page = "signup"
    num = ''
    err = ''
    success = ''
    form = CustomUserCreateForm()
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            num = request.POST.get('phone')
            user = form.save(commit=False)
            user.username = user.username.lower()
            name = request.POST.get('first_name')
            user.save()
            if len(num) == 11:
                if num[0:3] == "013" or num[0:3] == "017" or num[0:3] == "018" or num[0:3] == "019" or num[0:3] == "015" or num[0:3] == "016":
                    api = 'dTUsZl0CvtmvDF35kQY1'
                    rec = num
                    msg = f"Welcome {user.first_name} To Our Developers Community Platform DCOMM . Thank You"
                    
                    response = requests.post('http://bulksmsbd.net/api/smsapi?api_key='+api+'&type=text&number='+rec+'&senderid=8809617611061&message='+msg+'').json()
                    if response["error_message"] != "":
                        print("error")
                    else:
                        print("SCC")
                else:
                     print("NO")
            else:
                print("NO 2")
            messages.success(request,"User Create Successfully !!!")
            return redirect('login')
        else:
            print(form)
            messages.error(request,"Something Wrong !!! ")
            return redirect('signup')
    context = {"page":page,"userForm":CustomUserCreateForm}
    return render(request,"users/signup.html",context=context)
    

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST' and page == 'login':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request,'Username Not Found !!')
        
        user  = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'editAccount')
        else:
            messages.error(request,'Username Or Password is Incorrect !!')
    context = {"page":page}
            
    return render(request,'users/login.html',context=context)

@login_required(login_url='login')
def userAccount(request):
    p = Profile.objects.get(username=request.user.username)
    projects = request.user.profile.project_set.all()
    topSkills =  request.user.profile.skill_set.exclude(description__exact="")
    otherSkills =  request.user.profile.skill_set.filter(description="")
    print(projects)
    context = {"user":p,"projects":projects,"topSkills":topSkills,"otherSkills":otherSkills}
    return render(request,'users/user.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    pro = profile.id
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    projects = profile.project_set.all()
    context = {"user":profile,"topSkills":topSkills,"otherSkills":otherSkills,"projects":projects,"pro":pro}
    return render(request,'users/user-profile.html',context=context)


@login_required(login_url="login")
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form1 = SkillForm(request.POST)
        if form1.is_valid():
            skill1 = form1.save(commit=False)
            skill1.owner = profile
            skill1.save()
            messages.success(request,"Skill Add Successfully !!!")
            return redirect('user')
        else:
            messages.error(request,"Something Wrong !!!")
            return redirect('user')
    context = {"form":form}
    return render(request,'users/skill.html',context)


@login_required(login_url="login")
def updateSkill(req,pk):
    profile = req.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if req.method == "POST":
        form1 = SkillForm(req.POST,instance=skill)
        if form1.is_valid():
            form1.save()
            messages.success(req,"Skill Update Successfully !!!")
            return redirect('user')
        else:
            messages.error(req,"Something Wrong !!!")
            return redirect('user')

    context = {"form":form}
    return render(req,'users/update-skill.html',context)

@login_required(login_url="login")
def deleteSkill(req,pk):
    profile = req.user.profile
    skill = profile.skill_set.get(id=pk)
    if req.method == "GET":
        skill.delete()
        messages.success(req,"Skill Delete Successfully !!!")
        return redirect('user')

    return redirect('user')



@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests':messageRequests,"unread":unreadCount}
    return render(request,'users/messages.html',context)

@login_required(login_url="login")
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False :
        message.is_read = True
        message.save()
    context = {"message":message}
    return render(request,'users/message.html',context)


def sendMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.first_name
                message.email = sender.email
            message.save()

            messages.success(request,"Message Send Successfully !!!")
            return redirect('user-profile', pk=recipient.id)

    context = {"recipient":recipient,'form':form}
    return render(request,'users/message_form.html',context)