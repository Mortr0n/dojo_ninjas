from django.shortcuts import redirect, render, HttpResponse
from .models import Dojos, Ninjas


def index(request):
    context={
        "all_dojos" : Dojos.objects.all(),
        "all_ninjas" : Ninjas.objects.all(),
        
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    new_dojo = Dojos.objects.create(name=request.POST['name_input'], city=request.POST['city_input'], state=request.POST['state_input'], desc = request.POST['desc_input'])
    return redirect('/')


