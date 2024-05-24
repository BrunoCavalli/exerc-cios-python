numero = int(input("numero:"))

def numero_perfeito(numero):
    s_div = 0
    for i in range(1, numero):
        if numero % i == 0:
            s_div += i
    return s_div == numero

if numero_perfeito(numero):
    print(f"{numero} eh pefeito")
else:
    print(f"{numero} n eh perfeito")

#numero_perfeito = lambda num: sum(i for i in range(1, num) if num % i == 0) == num
#nao gostei do lambda tokar e tironi