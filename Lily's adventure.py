#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pushpita
#
# Created:     13/02/2024
# Copyright:   (c) Pushpita 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
while True:
  print('''1.roll the dice    2.To exit ''')
  user = int(input("what you want to do\n"))
  if user==1:
    number = random.randint(1,6)
    print(number)
  else:
    break