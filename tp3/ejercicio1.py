import re


patron = r'^[^._-][\w\d._-][^._-]+@[a-z]+(\.(com|edu|org|net|gov))?(\.(ar|br|cl|es|pe))?$'

emails = [
    'nombre@dominio.com',      # Válido
    'nombre@dominio.edu',      # Válido
    'nombre@dominio.org',      # Válido
    'nombre@dominio.net',      # Válido
    'nombre@dominio.gov',      # Válido
    'nombre@dominio.ar',       # Válido
    'nombre@dominio.br',       # Válido
    'nombre@dominio.cl',       # Válido
    'nombre@dominio.es',       # Válido
    'nombre@dominio.pe',       # Válido
    'nombre@dominio.com.ar',   # Válido
    'nombre@dominio.com.ar.ar',# No válido
    'nombre@dominio.mx',       # No válido
    'nombre@dominio.us'        # No válido
]

# Validar cada correo electrónico en la lista
for email in emails:
    if re.match(patron, email):
        print(f'{email} es un correo electrónico válida')
    else:
        print(f'{email} no un correo electrónico válida')
