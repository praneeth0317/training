# a fanction is a resuable piece of code that performs specific task 
# a function with parameters
# default return type for funtion 
# functions doesnt have default keyword use def keyword

def greetings():
    print("Welcome to functions concept")
# calling a function o invoking function
greetings()
print(greetings())
#with parameters
def greetings(name,age):
    print(f"{name} is {age} old")
greetings("python",40)
#
greetings(30,"js")

#keyword arguments
def sum(a= 0,b= 500):
    return a + b
result = sum(5,10)
print(result)
#keyword argu
result_2 = sum(b=100,a=10)
print(result_2)
#print(reslut_2(a=10,c=20))
print(sum())
print(sum(100))

# variable length arguments(*)
def sum(a,b,*c):
    return f"{a+b} and unused values are {c}"
print(sum(10,20,30))
print(sum(10,20,30,40,50))
# keyword length arguments(**)
def welcome(name,**temp):
    print(f"{name} welcome to datascience")
    print(temp)
welcome("ravi",id=101,age=51)

#lambda function a function without a name and one time use 
# syntax lanbda arguments:action
n = int(input("enter n value: "))
d = lambda x:x*x
d(n)
#Largest num of 2
result = lambda a,b:f"a vaue {a} is largest number" if a > b else f"b value {b} is largest number"
print(result(5,10))
# map is used apply some functions to each and every elements in sequence
# map(function,sequence)
r = [];
for i in 1:
    r.append(i*5)
print(1,r)
result = map(lambda x:x)