from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza




def index(request):



    '''pizzas = Pizza.objects.all()
    pizzas_info = [f"{pizza.nom} : {pizza.prix}€" for pizza in pizzas]
    pizzas_info_str = " . ".join(pizzas_info)
    return HttpResponse("les pizzas"  + pizzas_info_str)'''
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})