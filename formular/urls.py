from django.urls import path
from .views import HomeView, contact_form, confirmation, cancel_submission

urlpatterns = [
#    path('formular/', contact_form, name='contact_form'),
    path('formular/', HomeView, name='formular'),
    path('confirmation/', confirmation, name='confirmation'),
    path('cancel/', cancel_submission, name='cancel_submission'),
]
