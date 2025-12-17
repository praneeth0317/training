print(float("10"))
print(float("100.5"))
print(float(False))

# converting str to complex
print(complex("10"))
print(complex("10.5"))
print(complex(100,5))
print(complex(True,False)) 

#logical operators
print(10 and 0)
print(0 and "")
print("" and 0)
print(" " and "py")
print(False and True) 

a = 10
print(id(a),a)
b = 10
print(id(b),b)
print(a is b)
b = 50
print(a is b)

a = int(input("enter a number "))
b = int(input("enter a number "))
c = int(input("enter a number "))
if (a>b and a<c or a<b and a>c):
    print("a is greater")
elif(b>a and b<c or b<a and b>c):
    print("b is greater")
else:
    print("c is greater")

sum = 0
for i in range(1,11):
    sum += i
print(sum)