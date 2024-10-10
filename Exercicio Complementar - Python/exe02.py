# Somar os dígitos de um número menor que 100:

def somar_digitos(numero):
    if numero < 100:
        return sum(int(digito) for digito in str(numero))
    else:
        return "Número inválido"
print(somar_digitos(56))
