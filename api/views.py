from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def index(request):
    if request.method == "POST":
        nombre =  request.POST["nombre"]
        numero = request.POST["whatsapp"]
        # to see data on terminal
        # data_text = request.POST["text-data"].replace("\r\n", "\n")
        # print(data_text);
        text = request.POST["text-data"]
        context = {
            "nombre": nombre,
            "numero": numero,
            "text": text,
        }
        print("context", context)
        new_person = Conversation(nombre=nombre, numero=numero, text=text)
        new_person.save()
        print("nueva persona", new_person)
        return render(request, "api/index.html", context)
    else:
        return HttpResponse("Method == GET")

def conv(request):
    print("a")
    context = {
        "convos": Conversation.objects.all()
    }
    return render(request, "api/conv.html", context)