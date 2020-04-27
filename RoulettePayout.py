#RoulettePayout
#use randrange to get random number which has to be imported from random
#Notes/Problems
#use elif instead of else if there is another condition to be met
#be cautious of when the if statement starts and ends
#make sure print statements are correct
#check if the number comparisons are correct
from random import randrange
num = randrange (0, 38)
if num ==37:
    print("The result is 00")
else:
    print("The result is ... " + str(num))
if num == 37:
    print("Pay 00")
else:
    print("Pay", num)
if num % 2 == 1 and num >1 and num <9 or num % 2 == 0 and num > 12 and num <18 or num % 2 == 1 and num > 19 and num < 27 or num % 2 == 0 and num > 30 and num < 36:
    print ("Pay Red") 
elif num == 0 or num == 37:
    pass
else:
    print("Pay Black")
if num > 1 and num < 18:
    print("Pay 1 through 18")
elif num > 19 and num < 36:
    print("Pay 19 through 36")