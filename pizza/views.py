from django.shortcuts import render
from api.models import Pizza 

def templateHello(request):
    eredmeny = 54*31
    return render(request, 'hello.html', {"eredmeny":eredmeny, "pelda":"Aloha"})

def templatePizza(request):
    pizzas = []
    for pizza in Pizza.objects.all():
        pizzas.append({"name":pizza.name, "price":pizza.price, "img":pizza.img})

    return render(request, 'pizza.html', {"pizzas":pizzas})