while True:
    t = int(input(""))
    if t >0 and t<5:
        break
participantes = list(input())

retorno = participantes.count(str(t))
print(retorno)
