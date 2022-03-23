import random as rnd

#We used names as well as ID numbers to grill
#We number the topics by:
#0 - Linear equations
#1 - Finding roots
#2 - Approximations
#3 - Integration
types = ["Liner qeuations","Finding roots","Approximations","Integration"]
names = ["eden","alex"]
edenID = [2,0,8,3,7,6,0,9,5]
alexID = [3,2,1,2,2,3,0,7,5]
x=rnd.choice(names)
print(x)

# So we can grill a digit only between 0-3We will use Modulo 3
if (x=="eden"):
    y=rnd.choice(edenID)
    index = y%4
    print(index)
if (x=="alex"):
    y=rnd.choice(alexID)
    index = y%4
    print(index)


print("our grill is:")
print(types[index])