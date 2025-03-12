t = int(input("Informe o chá a ser avaliado: "))

participantes = [1,2,3,4,4]

if t <1 or t >4:
    print("erro")

retorno = participantes.count(t)
print(retorno)
