#Lab1 completed
print("Test")
a=5
b=5
c=5
print(a,b,c)
fruits=["apple","pear","peach"]
s1,s2,s3=fruits
print(s1,s2,s3)
y=str(1)
u=str(0)
i=str(1)
print(y+u+i)
#or
y=1
u=0
i=1
print(str(y)+str(u)+str(i))
#glogal x -комманда, которая объявит переменную x глобальной. И если поменять её значение в любой из функций, то даже в другой функции, она будет иметь новое значение.
carname="Mustang"
import random
print(random.randrange(1,10))
x = str("s1")
y = str(2) 
z = str(3.0894561) 
print(x,y,z)
st="""Test,
Very
Simple
Test.
"""
print(st)
for q in "flapple":
  print(q)
#for g in 505:
#  print(g)   -not work
print (len(st))
print("fire" in st)
print("fire" not in st)
print("Test" in st)
#or
if "Test" in st:
    print("True")
b = "Good Bye, World!"
print(b[0:len(b)])#last position not included
print(b[5:])
print(b[-6:-1])
k="test"
print(k.upper())
n=k.upper()
print(n.lower())
k="   Te st    "
print(k.strip())
print(k.replace("T", "e"))#меняет все T на e
#print(k.split(","))  returns ['Bye', ' World!']
pos=56
name="Somebody"
petition="You name {} and pos {}"
print(petition.format(name,pos))#формат вставляет в скобочки значение
#or boring joke
petition="You name {1} and pos {0}"
print(petition.format(name,pos))
cake="The \"Cake\" is lie"
print(cake)