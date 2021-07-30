from typing import Counter
from django.shortcuts import redirect, render, HttpResponse
from .models import Dojos, Ninjas


def index(request):
    context={
        "all_dojos" : Dojos.objects.all(),
        "all_ninjas" : Ninjas.objects.all(),
        # "ninja_count" :  Dojos.objects.values('ninja') 
        
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    new_dojo = Dojos.objects.create(name=request.POST['name_input'], city=request.POST['city_input'], state=request.POST['state_input'], desc = request.POST['desc_input'])
    return redirect('/')

# sidelining for later.  Want to put a count of ninjas per dojo
# def count(request):
#     c = Counter(Dojos.objects.filter(id=Dojos.ninja))
#     return c

def add_ninja(request):
    # Create a variable to grab the value from the dojo_input from the html.  This case the ID
    this_dojo = Dojos.objects.get(id=request.POST['dojo_input'])
    # When assigning a value to the Dojo item make sure to use the variable only.  
    # Don't make the mistake of formatting it like the other items which are grabbing from the request.POST method!
    # we are passing the entire this_dojo object in during the create statement.
    new_ninja = Ninjas.objects.create(first_name=request.POST['first_name_input'], last_name=request.POST['last_name_input'], dojo=this_dojo)
    return redirect('/')

def delete_ninja(request):
    ninja_to_delete = Ninjas.objects.get(id=request.POST['ninja_id'])
    # ninja_to_delete = Ninjas.objects.filter(id=ninjas_id)
    ninja_to_delete.delete()
    return redirect('/')