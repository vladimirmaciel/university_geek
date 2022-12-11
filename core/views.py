from django.shortcuts import get_object_or_404, render

from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        "curso": "Programação Web com Django Framework",
        "outro": "Django é massa!",
        "produtos": produtos,
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    # print(dir(Produto.objects))
    prod = get_object_or_404(Produto, id=pk)

    context = {"produto": prod}
    return render(request, "produto.html", context)
    # print(f"PK: {pk}")
    # return render(request, "produto.html")
