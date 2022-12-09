from django.shortcuts import render


def index(request):
    # print(dir(request))
    # print(f"{request.method}")
    # print(f"{request.headers}")
    # print(f"{request.headers['User-Agent']}")
    # print(f"{request.headers['host']}")
    # print(f"{request.headers['Cookie']}")
    # print(f"{request.user}")
    print(dir(request.user))
    # print(dir(request.user.username))
    # print(request.user.last_name)
    # print(request.user.password)
    # print(request.user.email)
    # print(request.user.is_superuser)

    # print(f"{request.get_port}")
    if str(request.user) == "AnonymousUser":
        teste = "Usuário não logado"
    else:
        teste = f"Usuário logado: {request.user}"
    contexto = {
        "curso": "Programação web com Django Framework",
        "outro": "Django é massa",
        "logado": teste,
    }
    return render(request, "index.html", context=contexto)


def contato(request):
    return render(request, "contato.html")
