# #Factorial
# def fact(n):
#     if(n==1):
#         return n
#     return n*fact(n-1)

# print(fact(5))


# #Largest No

# def lar(lst):
#     max = 0
#     for i in lst:
#         if(max<i):
#             max = i
#     print(max)

# lst =[1,5,8,7,9]
# lar(lst)


# def cir():
#     r = int(input())
#     print(3.14*r*r)

# def tri():
#     l = int(input())
#     b = int(input())
#     print(0.5*l*b)

# def sq():
#     n = int(input())
#     print(n*n)

# def rect():
#     l = int(input())
#     b = int(input())
#     print(l*b)

# cir()
# tri()
# sq()
# rect()


# def summ(lst):
#     sum = 0
#     for i in lst:
#         sum+=i
#     print(sum)

# lst = [1,2,3,4,5]
# summ(lst)

# def add():
#     a = int(input())
#     b = int(input())
#     print(a+b)
# def sub():
#     a = int(input())
#     b = int(input())
#     print(a-b)

# ch='y'
# while(ch=='y'):
#     print(''''
#     '1.add'
#     '2.sub''')
#     choice=int(input())
#     if(choice==1):
#         add()
#     elif(choice==2):
#         sub()
#     else:
#         ch=input("Do you want")
#         if(ch!='y'):
#             print("Thank you")


def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

print(gcd(10,20))