from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('data',views.data,name='data'),
    path('detect',views.detect,name='detect'),
    path('logout',views.logout,name='logout')
   
]