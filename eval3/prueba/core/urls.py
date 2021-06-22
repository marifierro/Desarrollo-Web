from django.urls import path
from .views import home, form_libro, registro


urlpatterns= [
    path('', home, name="home"),
    path('form-libro', form_libro, name='form_libro'),
    path('registro', registro, name='registro'),
    ]  
