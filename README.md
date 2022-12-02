# Zion Cloud

Ferramenta de backup com gerenciamento através da web.
Realiza transferência de dados através de SSH ou localmente (útil para compartilhamentos de máquinas Windows montadas por smb)

## Funções da ferramenta

- [ ] Gerenciamento de clientes
- [ ] Gerenciamento de servidores
- [ ] Gerenciamento de regras de backup
- [ ] Gerenciamento de execuções
- [ ] A ferramenta pode ser configurada como servidor principal ou cliente (para gerenciamento remoto).


## Para executar o backend em ambiente de desencolvimento

Configure um virtual environment do jeito que achar melhor.
```bash
python -m venv .venv
source .venv/bin/activate
```
Dentro do virtual environment, instale as dependencias da pasta requirements.
```bash
python -m pip install -r backend/requirements.txt
```
Caso queira "futricar" no projeto, recomendo instalar as dependências de DEV.
```bash
python -m pip install -r backend/requirements-dev.txt
```

Execute o arquivo contrib/env_gen.py para gerar seu arquivo .env


## Para executar o frontend em ambiente de desencolvimento
Instale as dependências do node.
```bash
cd frontend
npm install
```

Execute o servidor.
```bash
npm run serve
```

TODO Colocar a url do backend em variável global
TODO Adicionar a url do frontend para a constante CORS_ALLOWED_ORIGINS em settings.py
