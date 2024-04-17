from django.urls import path
#from .views import formular, success
from .views import HomeView, thank_you

urlpatterns = [
#    path('success/', success, name='success'),
    path('formular/', HomeView, name='formular'),
#    path('formular/', thank_you, name='thank-you'),
]
