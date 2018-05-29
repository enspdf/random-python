import enum

class TipoUsuario(enum.Enum):
    cliente = 1
    administrador = 2
    gerente = 3
    desarrollador = 4

# Name del enumerador
print(TipoUsuario.cliente.name)

# Value del enumerador
print(TipoUsuario.cliente.value)

# Acceder por atributo al name enumerador
print(TipoUsuario['gerente'].name)

# Acceder por atributo al value del enumerador
print(TipoUsuario['gerente'].value)

# Validación de tipos con el enumerador
print(TipoUsuario.cliente is TipoUsuario['cliente'])