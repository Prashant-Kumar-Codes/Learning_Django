from django.urls import path
from . import views     # use . for current directory


urlpatterns = [

#localhost: 8000/homepage
    path('', views.homepage, name = 'homepage')

#for localhost: 8000.webapp/about
   # path('about', views.about, name='about')
]
