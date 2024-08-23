from ex_1 import calcula_quant_triangulos

def test_calcula_quant_triangulos():
    assert isinstance(calcula_quant_triangulos(120), int)
    assert isinstance(calcula_quant_triangulos(10), int)
    assert isinstance(calcula_quant_triangulos(5), int)
    assert isinstance(calcula_quant_triangulos(2), int), "O valor 2 não é um valor válido para a função, pois não é possível formar um triângulo com 2 lado"
    assert isinstance(calcula_quant_triangulos(1), int), "O valor 1 não é um valor válido para a função, pois não é possível formar um triângulo com 1 lado"
    assert isinstance(calcula_quant_triangulos(-2), int), "O valor -2 não é um valor válido para a função, pois não é possível formar um triângulo com -2 lado"
    assert isinstance(calcula_quant_triangulos(0), int), "O valor 0 não é um valor válido para a função, pois não é possível formar um triângulo com 0 lado"
    assert isinstance(calcula_quant_triangulos(-10), int), "O valor -10 não é um valor válido para a função, pois não é possível formar um triângulo com -10 lado"

test_calcula_quant_triangulos()