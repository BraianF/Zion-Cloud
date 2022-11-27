# Zion Cloud

Ferramenta de backup com gerenciamento através da web.
Utiliza rsync para transferência de dados, através de SSH ou localmente (útil para compartilhamentos de máquinas Windows montadas por smb)

## Funções da ferramenta

- [ ] Gerenciamento de clientes
- [ ] Gerenciamento de servidores
- [ ] Gerenciamento de regras de backup
- [ ] Gerenciamento de execuções
- [ ] A ferramenta pode ser configurada como servidor principal ou cliente (para gerenciamento remoto).

## Testes


Configure um virtual environment do jeito que achar melhor.
```bash
python -m venv .env
```

Instale as dependencias da pasta requirements.
```bash
python -m pip install -r backend/requirements.txt
```

Caso queira "futricar" no projeto, recomendo instalar as dependências de DEV.
```bash
python -m pip install -r backend/requirements-dev.txt
```

