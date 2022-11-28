from pathlib import Path

from backups.models import Backup
from customers.models import Customer
from servers.models import Server
from django.conf import settings
from django.core.management.base import BaseCommand
from rich import print

# BKP_CONFIG_DIR = Path("/etc/zion/conf.d")
BKP_CONFIG_DIR = Path("/tmp/zion/conf.d")
BKP_CONFIG_DIR.mkdir(parents=True,exist_ok=True)

TEMPLATE_FILE = settings.BASE_DIR.parent / "utils/template.conf"

class Command(BaseCommand):
    help = 'Registra os arquivos de configuracao na pasta de controle do Zion'

    def handle(self, *args, **options):
        backup_list = Backup.objects.all()
        for backup in backup_list:
            file_name = backup.__str__().replace(" ","").replace(".","")
            
            base_file_path = BKP_CONFIG_DIR / file_name
            conf_file_path = Path(str(base_file_path) + ".conf")
            rules_file_path = Path(str(base_file_path) + ".rules")
            
            config = TEMPLATE_FILE.read_text()
            config = config.replace(
                "{backup_name}", f"backup_name = {backup.description}"
                ).replace(
                "{source_host}", f"source_host = {backup.server.ip_address}"
                )
            
            rules = backup.source_folders
            rules = rules + "\n- *"
            
            conf_file_path.write_text(config)
            rules_file_path.write_text(rules)
            
            
        print("done")
        
