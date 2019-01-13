from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Dictionary to pass to template engine
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page<br /><a href=\"/\">Home</a>")
