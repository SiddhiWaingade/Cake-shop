"""
URL configuration for cakeshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.show),
    path('dsp/', views.display),
    path('ct/', views.present),
    path('bd/', views.shown),
    path('fd/', views.feed),
    
    path('run/',views.run),
    path('run/home',views.home),

    path('home/',views.home),

    path('run/wdd',views.showed),
    path('run/test',views.show),

    path('run/abt',views.a),
    path('run/con',views.b),
    path('run/fd',views.feed),
  
   
    path('run/bdd',views.seen),
    path('run/dsp', views.display),

    path('run/ctt',views.see),
    path('run/ct', views.present),
  
    path('run/btd',views.look),
    path('run/bd', views.shown),
   
   

    path('check/', views.receive,name="book"),
    path('chek/', views.doOrder,name="orders"),
    path('chr/', views.future,name="christ"),
    path('bdy/', views.past,name="bday"),
    path('fback/', views.doFeedback,name="feedb"),
    path('rpt1/', views.reporder),
    path('rpt2/', views.reporder2),
    path('rpt3/', views.reporder3),
    path('rpt4/', views.reporder4),
    path('rpt5/', views.reporder5),
        
        
    
   ]
