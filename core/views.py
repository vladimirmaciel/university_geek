from django.shortcuts import render

def index(request):
    contexto = {
        "curso":"Programação web com Django Framework",
        "outro":"Django é massa"
    }
    return render(request, 'index.html', context=contexto)

def contato(request):
    return render(request, 'contato.html')
