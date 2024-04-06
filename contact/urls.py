from django.urls import path
from .views import showTest, showResult

urlpatterns = [
    path('test/', showTest, name='test'),
    # Add other URL patterns here
    path('result/', showResult, name='result'),
]
