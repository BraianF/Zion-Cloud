import uuid

from customers.models import Customer
from django.db import models


class Server(models.Model):
    hostname = models.CharField(max_length=45)
    description = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Descrição"
    )
    customer = models.ForeignKey(
        Customer,
        related_name="server",
        on_delete=models.CASCADE,
    )
    ip_address = models.CharField(
        max_length=15, blank=True, null=True, unique=True, verbose_name="Endereço IP"
    )
    ssh_user = models.CharField(
        max_length=100, default="root", verbose_name="Usuário de autenticação"
    )
    ssh_port = models.PositiveIntegerField(default=4502, verbose_name="Porta SSH")
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    
    created = models.DateTimeField(
        auto_now_add=True, editable=False, help_text="Criação"
    )
    updated = models.DateTimeField(auto_now=True, help_text="Atualização")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hostname} - {self.customer}"

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        # ordering = ['id']
