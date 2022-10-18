from django.contrib import admin
from django.urls import path
from venom import views

urlpatterns = [
    path("",views.signin,name='signin'),
    path('login/about/',views.about,name='about'),
    path('login/contact/',views.contact,name='contact'),
    path('login/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('msgsent/',views.msgsent,name='msgsent'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('movie1/',views.movie1,name='movie1')


   


   
    

    
]

