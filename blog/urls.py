#all these come from /blog

#access the functions from the views directory
from . import views 

# similar to the the project level urls.py 
from django.urls import path


urlpatterns = [
    path('', views.home, name='blog-home'), #empty first arg means homepage
    path('about/', views.about, name='blog-about'),
     
] #empty path, function that we created in views, and call it blog-home
#keep the name generic so you can add different apps with different homes
#this comes from the project-level django project