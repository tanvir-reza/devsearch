from django.urls import path
from .views import index,projects,project,createProject,updateProject,deleteProject

urlpatterns = [
    path('',projects,name='projects'),
    path('project/<str:pk>',project,name="project"),
    path('create-project/',createProject,name='createProject'),
    path('update-project/<str:pk>',updateProject,name='updateProject'),
    path('delete-project/<str:pk>',deleteProject,name='deleteProject'),

]
