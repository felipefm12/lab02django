

from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    #1path('', views.index,name='index'),
    #1path('enviar', views.enviar,name='enviar'),
    
    path('', views.indexmatematico,name='indexmatematico'),
    path('enviar2', views.enviar2,name='enviar2'),
    
    #2path('', views.indexcilindro,name='indexcilindro'),
    #2path('calcular', views.calcular,name='calcular'),
   
]
