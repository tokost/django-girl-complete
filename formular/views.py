from django.shortcuts import render, redirect
from formular.forms import ContactForm
from django.http import HttpResponse

from django.http import request
from django.core.mail import send_mail
from django.conf import settings



def formular(request):
    s = "<h1> Toto je formular z views.</h1>"
#    return render(request, 'formular.html', {'form': form})
    return HttpResponse(s)

def success(request):
   return HttpResponse('Success z views !')

'''
def HomeView(request):
    return render(request,'index.html')
#    s = "<h1> Toto je formular z views aplikacie formular.</h1>"
#    return HttpResponse(s)
'''


def HomeView(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        msg_mail = str(message) + "\n\nFrom: " + str(message_email)

        send_mail(
            "Contacted by " + message_name,
            msg_mail, 
            message_email, 
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        return render(request, 'index.html', {'message_name': message_name, 
                                              'message_email': message_email, 
                                              'message': message})
    else:
        return render(request, 'index.html', {})