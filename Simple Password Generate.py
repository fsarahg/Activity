import random
p = int(input("Enter length of password :"))
x="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
y =  "".join(random.sample(x,p))
print (y)
