"""resolução exercicio 1 da lista de Linguagens de programação"""

def calcula_quant_triangulos(valor):

    triangulos_max = 0
    perimetro_max = 0

    for valor in range(3, valor + 1):
        triangulos = valor * (valor - 1) * (valor - 2) // 2

        if triangulos > triangulos_max:
            triangulos_max = triangulos

        return triangulos
    
print(calcula_quant_triangulos(0))

