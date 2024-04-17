"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from blog import views as blog_views    # aby nebol konflikt tak sa pri views uvedu
from contact import views as contact_views  # nazvy aplikacii z ktorych sa stranky tahaju
from mysite.views import success

# from formular import views as formular_views

# from formular.views import formular, success

urlpatterns = [
# Toto su nainstalovane aplikacie
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
#    path('contact/', include('contact.urls')),
    path('formulars/', include('formular.urls')),

    path('test/', contact_views.showTest),
    path('result/', contact_views.showResult),

# Pre multi aplikcie v jednom projekte
    path('about/', blog_views.about),
#    path('contact/', blog_views.showContact),
    path('', blog_views.greeting),  # naskakuje ale stranka z blog.urls

# Pre kontktnuy formular
#    path('formular/', formular_views.formular),
    path('success/', success, name = 'success'),
]
 
