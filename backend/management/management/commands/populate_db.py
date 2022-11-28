from random import choice

from customers.models import Customer
from servers.models import Server
from django.core.management.base import BaseCommand
from faker import Faker
from rich import print


def create_customer(fake: Faker):
    razao_social = fake.company()
    inscricao_federal = fake.company_id()
    phone = fake.phone_number()
    email = fake.ascii_company_email()
    
    c = Customer(razao_social=razao_social, inscricao_federal=inscricao_federal, phone=phone, email=email)
    c.save()

def create_server(fake: Faker):
    hostname = fake.hostname()
    description = fake.sentence()
    ip_address = fake.ipv4_private()
    
    pks = Customer.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    customer = Customer.objects.get(pk=random_pk)
    
    s = Server(hostname=hostname, description=description, ip_address=ip_address, customer=customer)
    s.save()

class Command(BaseCommand):
    help = 'Popula o banco de dados com clientes e servidores ficticios.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('quantity', nargs='?', default=1, type=int)

        # Argumento nomeado
        parser.add_argument(
            '--customer', '-c',
            action='store_true',
            help='Cria clientes.'
        )
        parser.add_argument(
            '--server', '-s',
            action='store_true',
            help='Cria servidores.'
        )

    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        
        if options['quantity'] < 1:
            print('É melhor que a quantidade seja um valor positivo maior que zero.')
            return None
        
        if options['customer']:
            print('Criando cliente(s)...')
            for _ in range(options['quantity']):
                print(f'{_+1} de {options["quantity"]}')
                create_customer(fake)
            
            print('Concluído')
        
        if options['server']:
            if Customer.objects.all().count() > 0:
                print('Criando servidor(es)...')
                for _ in range(options['quantity']):
                    print(f'{_+1} de {options["quantity"]}')
                    create_server(fake)
                    
                print('Concluído')
            else:
                print('É necessário ter clientes cadastrados para criar servidores')
