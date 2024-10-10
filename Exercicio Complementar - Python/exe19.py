# Ler uma lista de 10 inteiros e imprimir a soma e a média:

def soma_media_lista():
    lista = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]
    soma = sum(lista)
    media = soma / 10
    return soma, media
soma, media = soma_media_lista()
print(f"Soma: {soma}, Média: {media}")
