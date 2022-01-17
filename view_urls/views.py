# from django.http import HttpResponse
from django.shortcuts import render
from . import machine_learning_model


def home(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def result(request):
    user_int = request.GET['user_int']
    user_int = machine_learning_model.multiplier(user_int)
    return render(request, 'result.html', {'home_input':user_int})
    
def adminpanel(request):
    return render(request, 'adminpanel.html')
    
# def result(request):
#     user_string = user_string.upper()
#     user_string += ': is the text you entered on the form.'
#     return render(request, 'result.html', {'home_input':user_string})
    
