from django.shortcuts import render
from django.urls import reverse

from django.http import HttpResponse

# from contact.mysite import mysite
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

# Contact Forms
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc = form.cleaned_data['cc']
        recipients = ['sender@example.com']
        recipients.append(sender)
        # Na odoslanie emailu daným príjemcom
        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
#    reverse('contact', args=())

# Pre multiple app
def showTest(request):
    s = "<h1>Kontaktná stránka z aplikacie contact</h1>"
    s += "<p>Webová stránka: tokos.sk</p>"
    s += "<p>Mobil: +421 907834599</p>"
    s += "<p>Email: tokos@comto.sk</p>"
    return HttpResponse(s)

def showResult(request):
    s = "<h1>Toto je stránka z aplikácie contact na ktorej sa zobrazia výsledky</h1>"
    return HttpResponse(s)
