from django.shortcuts import render, HttpResponse
from .models import Select, Question, Greeting
from datetime import datetime

# Create your views here.
def home(request):
    selects= Select.objects.all()
    questions= Question.objects.all()
    greet=Greeting.objects.get(pk=1) 
    hi= ""
    bye=""
    paragraph= []

    if request.method=='POST':
        #Greetings
        if "greet" in request.POST:
            horario=datetime.now()
            hora= horario.hour    
            if (hora>12) and (hora<20):
                hi= greet.afternoon
            elif (hora >=20) and (hora< 5):
                    hi= greet.night
            else:
                hi= greet.morning
        if "greet2" in request.POST:
            bye= greet.by

        #Selects
        paragraph = request.POST.getlist('sel')  
    
    return render(request, "generator/home.html", 
    {'selects':selects, 'questions':questions, 'hi':hi,'bye': bye, "paragraph":paragraph})

