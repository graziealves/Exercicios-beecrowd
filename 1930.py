t1,t2,t3,t4 =input ().split(" ")
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)
t4 = int(t4)

if not(t1==1 or t1>6 or t2==1 or t2>6 or t3==1 or t3>6 or t4==1 or t4>6):
    equipamentos = int(t1) -1 + int(t2)-1 + int(t3)-1 + int(t4)
    print(equipamentos)

