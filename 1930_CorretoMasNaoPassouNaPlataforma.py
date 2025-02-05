#t1, t2, t3,t4 = int(input()), int(input()), int(input()), int(input())

t1,t2,t3,t4 = list(input())
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)
t4 = int(t4)

if not(t1==1 or t1>6 or t2==1 or t2>6 or t3==1 or t3>6 or t4==1 or t4>6):
    equipamentos = int(t1) -1 + int(t2)-1 + int(t3)-1 + int(t4)
    print(equipamentos)


'''
entrada = list(input())

print(entrada)

t1= entrada[0]
t2 = entrada[1]
t3 = entrada[2]
t4 = entrada[3]
'''


