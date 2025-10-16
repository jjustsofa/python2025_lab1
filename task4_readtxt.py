import time
import math
import os
clear = lambda: os.system('cls')
RED='\u001b[41m'
RED1='\u001b[36m'
END='\u001b[0m'
BLUE='\u001b[44m'
WHITE='\u001b[40m'
GREEN='\u001b[42m'
ORANGE ='\u001b[43m'
ERASE='\x1B[2K'#erase the line
BEGIN='\x1B[1G'



f=open('sequence.txt')
all_num = []
for num in f:
    all_num.append(float((num)))

podh_num = []

for k in all_num:
    if math.ceil(k) < 0:
        podh_num.append(k)

more_than_five = []
less_than_five = []

for k in podh_num:
    if math.ceil(k) > -5:
        more_than_five.append(k)
    else:
        less_than_five.append(k)
mtf = (len(more_than_five) * 100) / len(all_num)
ltf = (len(less_than_five) * 100) / len(all_num)

print(mtf, f'{RED}{" " * int(mtf)}{BEGIN}{RED1}{"больше -5, но меньше 0"+' ' +str(mtf)}{END}')
print(ltf, f'{WHITE}{" " * int(ltf)}{BEGIN}{RED1}{"меньше -5 и меньше 0"+' ' +str(ltf)}{END}')



