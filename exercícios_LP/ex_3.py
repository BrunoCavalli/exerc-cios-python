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


retangulo_1 = ((1, 1), (4, 1), (4, 3), (1, 3))
retangulo_2 = ((3, 2), (6, 2), (6, 5), (3, 5))

print(retangulos_colidem(retangulo_1, retangulo_2)) 