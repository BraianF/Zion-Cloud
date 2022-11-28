from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    # Altera o campo de seleção para um mais inteligente
    autocomplete_fields = ["customer"]

    # Organização do formulário
    fieldsets = (
        (
            "Identificação",
            {
                "fields": (
                    "hostname",
                    "description",
                    "customer",
                ),
            },
        ),
        (
            "Dados de acesso",
            {
                "fields": (
                    "ip_address",
                    "ssh_user",
                    "ssh_port",
                    "token",
                ),
            },
        ),
        (
            "Informações adicionais",
            {
                "classes": ("collapse",),
                "fields": (
                    "created",
                    "updated",
                    "active",
                ),
            },
        ),
    )

    # Campos mostrados na lista
    list_display = (
        "id",
        "description",
        "customer",
        "ip_address",
        "ssh_port",
        "active",
    )

    # Campos com links para acessar o cadastro
    list_display_links = (
        "id",
        "description",
    )

    # Permite editar o campo do registro sem abrir o formulario
    list_editable = ("active",)

    # Cria filtro de registros ativos
    list_filter = ("active",)

    # Lista a quantidade de itens por página
    list_per_page = 25

    # Utiliza a função select_related() do django para salvar
    # algumas queries que envolvem chaves estrangeiras
    list_select_related = ("customer",)

    # Campos somente leitura, que vão aparecer nos forms
    readonly_fields = ("created", "updated")

    # Permite criar um novo item a partir deste já existente
    save_as = True

    # Mostra o botão de salvar no topo do formulario
    save_on_top = True

    # Campos de busca
    search_fields = (
        "hostname",
        "customer__razao_social",
        "customer__nome_fantasia",
    )


admin.site.register(Server, ServerAdmin)
