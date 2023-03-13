from django.urls import path
from .views import profiles,loginPage,logoutUser,signupUser,userAccount,editAccount,userProfile,addSkill,updateSkill,deleteSkill,inbox,viewMessage,sendMessage

urlpatterns = [

    path('login',loginPage,name='login'),
    path('logout',logoutUser,name='logout'),
    path('signup',signupUser,name='signup'),
    path('user',userAccount,name='user'),
    path('edit-profile',editAccount,name='editAccount'),
    path('user-profile/<str:pk>',userProfile,name='user-profile'),
    path('add-skill/',addSkill,name='addSkill'),
    path('update-skill/<str:pk>',updateSkill,name='updateSkill'),
    path('delete-skill/<str:pk>',deleteSkill,name='deleteSkill'),
    path('inbox',inbox,name='inbox'),
    path('message/<str:pk>',viewMessage,name='viewMessage'),
    path('send-message/<str:pk>',sendMessage,name='sendMessage'),
    path('',profiles,name='profiles'),

]
