from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animal

def animais(request):
    meusanimais= Animal.objects.all().values()
    template = loader.get_template('animais_cadastrados.html')
    context = {
        'meusanimais': meusanimais,
    }
    return HttpResponse(template.render(context,request))
def detalhes(request,id):
    meuanimal = Animal.objects.get(id=id)
    template = loader.get_template('detalhes.html')
    context = {
        'meuanimal': meuanimal,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'frutas' : ['Maça','Banana' , 'Cereja']
    }
    return HttpResponse (template.render(context,request))
