#Write a list of numbers v:
v = [1,2.56,-3.43,0]
print("v =>",v)

#Get a random number between 0 and 1:
import random
r = random.random()
print("\nr =>",r)

#Logical operators
print("\n<=: less than or equal to.\n<: smaller than.")
print(">=: greater than or equal.\n>: greater than.")
print("==: equal to.\n!=: distinct.")

#conditional
def multiple(n,m):
    if n%m == 0:
        print('Is divisible')
        return True
    else:
        print('Is not divisible')
        return False
#to open the file from the python console:
#exec(open("ejemplo.py").read())


