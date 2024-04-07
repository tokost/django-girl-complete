from django.shortcuts import render

from django.http import HttpResponse


def showTest(request):
    s="<h1> Toto je zobrazenie testovacej strnáky z aplikácie contact</h1>"
    return HttpResponse(s)

def showResult(request):
    s = "<h1> Toto je zobrazenie stránky výsledkov z aplikácie contact</h1>"
    return HttpResponse(s)
