from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Customer(models.Model):
    # Dados de registro
    razao_social = models.CharField(
        max_length=254, verbose_name="Razão Social / Nome"
    )
    nome_fantasia = models.CharField(
        max_length=254, verbose_name="Nome fantasia", blank=True, null=True
    )
    inscricao_federal = models.CharField(
        max_length=20, verbose_name="CNPJ / CPF", unique=True
    )
    
    # Dados de contato
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)

    # Dados adicionais
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criação")
    updated = models.DateTimeField(auto_now=True, verbose_name="Atualização")
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "customer"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        """String for representing de Model object."""
        if self.nome_fantasia is not None:
            return self.nome_fantasia
        
        return self.razao_social
    
    def get_absolute_url(self):
        return reverse_lazy('customer:detail-update-drestry', kwargs={'pk': self.pk})