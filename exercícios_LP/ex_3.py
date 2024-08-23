"""resolução exercício 3 da lista de Linguagens de programação"""

def verifica_se_é_retangulo(valor):
    # função que testa se o objeto é um retangulo
    if len(valor) != 4:
        print("não é um triangulo")
        return False
    
    for vertice in valor:
        if not isinstance(vertice, (int, float)):
            print("os vertices (x,y) tem que ser inteiros")
            return False
        
    return True


def retangulos_colidem(retan_1, retan_2):
    if not verifica_se_é_retangulo(retan_1) or not verifica_se_é_retangulo(retan_2):
        return None
    
    x1, y1, largura1, altura1 = retan_1 
    x2, y2, largura2, altura2 = retan_2

    # Verifica se os retângulos colidem
    colisao_x = not (x1 + largura1 < x2 or x2 + largura2 < x1)
    colisao_y = not (y1 + altura1 < y2 or y2 + altura2 < y1)

    return colisao_x and colisao_y

retan_1 = (0, 0, 40, 50)
retan_2 = (50, 50, 100, 100)


if retangulos_colidem(retan_1, retan_2):
    print("colide")
else:
    print("não colide")

