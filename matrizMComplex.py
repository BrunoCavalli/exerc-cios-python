M = int(input("Numero de linhas:"))
N = int(input("numero de colunas:"))

def cria_matriz(m, n):
    # Inicializa a matriz como uma lista vazia
    matriz = []
    
    # Inicializa o contador com o valor 1
    contador = 1
    
    # Preenche a matriz
    for i in range(m):
        # Cria uma nova linha
        linha = []
        for j in range(n):
            # Adiciona o próximo número na linha
            linha.append(contador)
            # Incrementa o contador
            contador += 1
        # Adiciona a linha completa na matriz
        matriz.append(linha)
    
    return matriz

# Exemplo de uso

matriz = cria_matriz(M, N)
for linha in matriz:
    print(linha)
