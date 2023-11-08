import random
Hhp = random.randrange(50,100)
Mhp = random.randrange(50,100)
count = 0

while (Hhp > 0 and Mhp > 0):
    Hatt = random.randrange(-10,20)
    Matt = random.randrange(-10,20)

    if Matt > 0:
        Hhp -= Matt
    print(f'hero(HP:{Hhp}, attck:{Hatt})', end = " ")
    if Hatt > 0:
        print(" success", end = " ")
    
    else:
    print(" fail", end = " ")
    if Hatt > 0:
        Mhp -= Hatt
    print(f' <-> monster(HP:{Mhp}, attck:{Matt})', end = " ")
    if Matt > 0:
        print(" success")
    
    else:
        print(" fail")
    count +=1

print ("----------------------------------")
print(f'Total phase: {count},')

if Hhp > 0:
    print('Hero Win!!!')
else:
    print('Monster Win!!!!')

