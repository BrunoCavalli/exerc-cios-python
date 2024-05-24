frase = input("sua frase:")
palavras = frase.split()
letra = input("sua letra:")
letra_p = []

for palavra in palavras:
    if letra in palavra.lower():
        letra_p.append(palavra)

print(letra_p)