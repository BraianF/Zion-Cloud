from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    # Texto apresentado se o valor do campo for vazio. Padrao '-'
    # empty_value_display = "-Não Definido-"

    # Organização do formulário
    fieldsets = (
        (
            "Identificação",
            {
                "fields": (
                    "razao_social",
                    "nome_fantasia",
                    "inscricao_federal",
                ),
            },
        ),
        (
            "Contato",
            {
                "fields": (
                    "phone",
                    "email",
                )
            },
        ),
        (
            "Informações adicionais",
            {
                "fields": (
                    "created",
                    "updated",
                    "active",
                )
            },
        ),
    )

    # Campos mostrados na lista
    list_display = (
        "id",
        "razao_social",
        "nome_fantasia",
        "phone",
        "email",
        "active",
    )

    # Campos com links para acessar o cadastro
    list_display_links = (
        "id",
        "razao_social",
    )

    # Permite editar o campo do registro sem abrir o formulario
    list_editable = ("active",)

    # Cria filtro de registros ativos
    list_filter = ("active",)

    # Lista a quantidade de itens por página
    list_per_page = 25

    # Campos somente leitura, que vão aparecer nos forms
    readonly_fields = ("created", "updated")

    # Permite criar um novo item a partir deste já existente
    save_as = True

    # Mostra o botão de salvar no topo do formulario
    save_on_top = True

    # Campos de busca
    search_fields = (
        "razao_social",
        "nome_fantasia",
    )


admin.site.register(Customer, CustomerAdmin)
