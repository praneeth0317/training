
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