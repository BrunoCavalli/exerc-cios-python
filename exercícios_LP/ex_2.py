# def preencher_matriz(m, n):
#     # Verificar se m < n e se m e n são primos entre si
#     if m >= n or not sao_primos_entre_si(m, n):
#         print("m e n não atendem aos requisitos.")
#         return None

#     matriz = [[0] * n for _ in range(n)]  # Criar matriz n x n preenchida com zeros
#     numero = 1  # Iniciar com o número 1

#     for i in range(n):
#         for j in range(n):
#             if (j + 1) % m == 0:  # Verificar se é um passo de m em m casas
#                 matriz[i][j] = numero
#                 numero += 1

#     return matriz

# def sao_primos_entre_si(m, n):
#     # Verificar se m e n são primos entre si usando o algoritmo de Euclides
#     while n != 0:
#         m, n = n, m % n

#     return m == 1

# print(preencher_matriz(2, 3 ))

def verifica_primo_entre_si(m, n):
    if m * n % 2 != 0:
        return False
    
print(verifica_primo_entre_si(8, 4))