#Number guessing program
from random import randint
a=(randint(0, 50))
print(a)
inp=int(input(("Enter the value")))
while(1==1):
  if(inp>a):
   print('Your Guess is above the number please inputcorrectly')
   inp=int(input(("continue the game")))
  elif(inp<a):
   print('Your Guess is below the number please inputcorrectly')
   inp=int(input(("continue the game")))
  else:
   print('congrats Your gusess is correct')
   break