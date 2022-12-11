from django.contrib import admin
from django.db import models
from django.utils.html import format_html


class Produto(models.Model):
    objects = models.Manager()

    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)
    estoque = models.IntegerField("Quantidade em estoque")

    def __str__(self) -> str:
        # return f"{self.nome} {self.estoque} {self.preco}"
        return f"{self.nome}"


class Clinete(models.Model):
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    email = models.EmailField("E-mail", max_length=100)

    def __str__(self) -> str:
        # return f"{self.nome} {self.sobrenome} {self.email}"
        return f"{self.nome}"
