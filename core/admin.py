from django.contrib import admin

from .models import Clinete, Produto


@admin.register(Clinete)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email")
    fields = ("nome", "sobrenome", "email")
    search_fields = ["sobrenome"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque")
    fields = ("nome", "preco", "estoque")
