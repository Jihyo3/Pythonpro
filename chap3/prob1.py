import random
mood = random.randrange(4)
print('you are ..')
if mood == 0: #happy
    print('-----------\n|  ^  ^   |\n| //   // |\n|   \/    |\n-----------')
#nuetral
elif mood == 1:
    print('----------\n|  o  o |\n|       |\n|    o  |\n----------')
#sad
elif mood == 2:
    print('------------\n|   -    -  |\n|           |\n|     /\    |\n------------')
else:
    print('Illegal mood value!')
print('...today.')

