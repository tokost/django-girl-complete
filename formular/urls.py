from django.urls import path
#from .views import formular, success
from .views import HomeView

urlpatterns = [
#    path('success/', success, name='success'),
    path('formular/', HomeView, name='formular'),
]
