from django.urls import path
#from .views import formular, success
from .views import HomeView

urlpatterns = [
#    path('formular/', formular, name='formular'),
#    path('success/', success, name='success'),
    path('formular/', HomeView, name='formular'),
]
