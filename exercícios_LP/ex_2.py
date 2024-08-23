"""resolução ex 2 da lista de Linguagens de programação"""

def verifica_primo_entre_si(m, n):
    while n != 0:
        m, n = n, m % n
    return m == 1

def gera_matriz(m, n):
    if m >= n or not verifica_primo_entre_si(m, n):
        print("m e n não atendem as condiçoes")
        return None
    
    matriz = [[0] * n for _ in range(n)]

    num = 1
    for i in range(n):
        posicao = 0
        while posicao < n:
            matriz[i][posicao] = num
            num += 1
            posicao += m

    return matriz

print(gera_matriz(3, 5))