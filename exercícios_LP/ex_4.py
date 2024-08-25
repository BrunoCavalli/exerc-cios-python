"""resolução ex 4 da lista de Linguagens de programação"""

def verifica_se_é_retangulo(valor):
    # função que testa se o objeto é um retângulo ou não
    if len(valor) != 4:
        print("não é um retângulo")
        return False
    
    for vertice in valor:
        if not (isinstance(vertice, tuple) and len(vertice) == 2 and
                isinstance(vertice[0], (int, float)) and isinstance(vertice[1], (int, float))):
            print("Os vértices (x, y) devem ser tuplas de dois números.")
            return False
        
    return True


def retangulos_colidem(retan_1, retan_2):
    if not verifica_se_é_retangulo(retan_1) or not verifica_se_é_retangulo(retan_2):
        return None
    
    # calcula os limites dos triangulos
    x1_min, y1_min = min(p[0] for p in retan_1), min(p[1] for p in retan_1)
    x1_max, y1_max = max(p[0] for p in retan_1), max(p[1] for p in retan_1)
    
    x2_min, y2_min = min(p[0] for p in retan_2), min(p[1] for p in retan_2)
    x2_max, y2_max = max(p[0] for p in retan_2), max(p[1] for p in retan_2)
    
    # Verifica se os retângulos colidem
    colisao_x = not (x1_max < x2_min or x2_max < x1_min)
    colisao_y = not (y1_max < y2_min or y2_max < y1_min)

    return colisao_x and colisao_y


def verifica_colisao(**Kwargs):
    colisoes = []
    nomes = list(Kwargs.keys())
    retangulos = list(Kwargs.values())

    if len(retangulos) < 2:
        return []
    
    # valida os retangulos
    for nome, ret in Kwargs.items():
        if not verifica_se_é_retangulo(ret):
            print(f"Retângulo '{nome}' inválido.")
            return []
    
    # Verifica a colisão entre os retangulos
    for i in range(len(retangulos)):
        for j in range(i + 1, len(retangulos)):
            if retangulos_colidem(retangulos[i], retangulos[j]):
                colisoes.append((nomes[i], nomes[j]))
    
    return colisoes



retangulo_1 = ((1, 1), (4, 1), (4, 3), (1, 3))
retangulo_2 = ((3, 2), (6, 2), (6, 5), (3, 5))
retangulo_3 = ((5, 5), (8, 5), (8, 7), (5, 7))

colisoes = verifica_colisao(a=retangulo_1, b=retangulo_2, c=retangulo_3) #  <--  como usar
print(colisoes)  