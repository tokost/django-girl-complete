from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def confirmation(request):
    return render(request, 'confirmation.html')


def cancel_submission(request):
    # Handle cancel action here
    # For example, redirect back to the form
    return redirect('contact_form')

'''
def HomeView(request):
    #    return render(request,'index.html')
    s = "<h1> Toto je stranka formular ktora pouziva z views HomeView bez sablony.</h3>"
    return HttpResponse(s)
'''

def HomeView(request, pk=None):
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
        render(request, 'index.html', {'message_name': message_name,
                                              'message_email': message_email,
                                              'message': message} )
        return redirect('confirmation')
#        return redirect('confirmation') # iba meno sablony kam sa presmeruje
    else:
        return render(request, 'index.html', {}) # zadany text sa skombinuje so sablonou 

def contact_form(request):
    if request.method == 'POST':
        # Process form submission

        # After processing, redirect to confirmation page
        return redirect('confirmation')
    else:
        # Render the contact form
        return render(request, 'contact_form.html')
