from servers.models import Server
from django.db import models


class Backup(models.Model):
    source_folders_help = """
    Se pretende copiar determinadas pastas presente em subpastas
    do caminho definido, deverá montar a estrutura até chegar nela
    <br>Exemplo:
    <pre>
    + /usr/
    + /usr/local/
    + /usr/local/bin/***
    + /var/
    + /var/spool/
    + /var/spool/cron/
    + /var/spool/cron/crontabs/***
    </pre>
    Se quer copiar tudo, manda brasa só nesse mesmo
    <br><pre>+ /***</pre>
    """

    additional_parameters_help = """
    Defina algumas opções adicionais do rsync se precisar.<br>
    O programa já usa por padrão as opções: '-avihh', '--stats', '--out-format=%i %C %n%L' e '--delete-excluded'.<br>
    As opções deverão ser separadas por um espaço.<br>
    Exemplo: <br>
    <pre>
    --compress --partial --progress
    </pre>
    """

    server = models.ForeignKey(
        Server,
        related_name="backup",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        help_text="Servidor que este backup pertence",
    )

    description = models.CharField(max_length=255, verbose_name="Descrição")

    # Dados de retenção do backup
    daily_retention = models.PositiveIntegerField(
        default=1, verbose_name="Retenção diária"
    )
    monthly_retention = models.PositiveIntegerField(
        default=0, verbose_name="Retenção mensal"
    )
    yearly_retention = models.PositiveIntegerField(
        default=0, verbose_name="Retenção anual"
    )
    logs_retention = models.PositiveIntegerField(
        default=1, verbose_name="Retenção dos logs"
    )

    # Dados de regras e parâmetros
    source_folders = models.TextField(
        default="+/***", help_text=source_folders_help
    )

    additional_parameters = models.CharField(
        max_length=255,
        verbose_name="Parâmetros adicionais do backup",
        null=True,
        blank=True,
        help_text=additional_parameters_help,
    )

    report_address = models.EmailField(
        null=True,
        blank=True,
        verbose_name="Endereço de notificação",
        help_text="Quer que o cliente saiba como está o backup dele? Coloque aqui.",
    )

    # Dados adicionais
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criação")
    updated = models.DateTimeField(auto_now=True, verbose_name="Atualização")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.description} - {self.server}"

    class Meta:
        verbose_name = "Backup"
        verbose_name_plural = "Backups"
        # ordering = ['id']
