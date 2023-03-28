# a=int(input("write A "))
# b=int(input("write B "))
# def function(a,b):
#     if b==0:
#         return 1
#     if b==1:
#         return a
#     return function(a,b-1)*a
# j=function(a,b)
# print(j)

a=int(input("write a "))
b=int(input("write b "))

def summ(a,b):
    if b !=0:
        return summ(a,b-1) + 1
    if a!=0:
        return summ(a-1,b) + 1
    return 0
j=summ(a,b)
print(j)

