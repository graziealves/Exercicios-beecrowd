entrada = list(input())
tomadas = []

print(entrada)

for e in entrada:
    if e !=" ":
        tomadas.append(int(e))

t1 = tomadas[0]
t2 = tomadas[1]
t3 = tomadas[2]
t4 = tomadas[3]

if not(t1==1 or t1>6 or t2==1 or t2>6 or t3==1 or t3>6 or t4==1 or t4>6):
    equipamentos = int(t1) -1 + int(t2)-1 + int(t3)-1 + int(t4)
    print(equipamentos)

print(tomadas)