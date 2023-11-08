inventory = ["sword", "armor", "shield", "healing potion"]
print('your items : ', inventory)
print('\nPress the enter key to continue.\n You have ',len(inventory),'items in your possession.\n')
print('Press the enter key to continue.')

if 'healing potion' in inventory:
    print('You will live to fight another day.\n')
index =int(input('Enter th index number for an item in inventory : '))
print('At index',index, 'is', inventory[index])

begin = int(input('\nEnter the index number to begin a slice: '))
end = int(input('Enter the index number to end the slice : '))
print ("inventory[", begin, ":", end, "] is:\t", inventory[begin : end], end = "")
print('\n\nPress the enter key to continue.')

chest = ['gold', 'gems']
print('You find a chest.\t It contains : \n', '<', chest[0:2],'>')

inventory += chest
print('\nYou add the contents of the chest to your inventory.\nYour inventory is now : \n',inventory)

