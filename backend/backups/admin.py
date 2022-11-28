from django.contrib import admin

from .models import Backup


class BackupAdmin(admin.ModelAdmin):
    # Altera o campo de seleção para um mais inteligente
    autocomplete_fields = ["server"]

    # Organização do formulário
    fieldsets = (
        (
            "Identificação",
            {
                "fields": (
                    "server",
                    "description",
                ),
            },
        ),
        (
            "Retenção",
            {
                "description": "Quantos dias/meses/anos você deseja manter seus backups?<br>Quantos logs devem ser armazenados?",
                "fields": (
                    "daily_retention",
                    "monthly_retention",
                    "yearly_retention",
                    "logs_retention",
                ),
            },
        ),
        (
            "Regras e parâmetros",
            {
                "fields": (
                    "source_folders",
                    "additional_parameters",
                    "report_address",
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
        "server",
        "report_address",
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
    list_select_related = ("server",)

    # Campos somente leitura, que vão aparecer nos forms
    readonly_fields = ("created", "updated")

    # Permite criar um novo item a partir deste já existente
    save_as = True

    # Mostra o botão de salvar no topo do formulario
    save_on_top = True

    # Campos de busca
    search_fields = (
        "description",
        "server__hostname",
        "server__cliente__razao_social",
        "server__cliente__nome_fantasia",
    )


admin.site.register(Backup, BackupAdmin)
