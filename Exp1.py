# #Swapping with Temp
# a = int(input())
# b = int(input())
# temp = a
# a = b
# b = temp
# print(a)
# print(b)


# #Swapping with without Temp
# a = int(input())
# b = int(input())
# a = a+b
# b = a-b
# a = a-b
# print(a)
# print(b)

# #Simple Interest and Compound Interest
# amt = int(input())
# t = int(input())
# r = float(input())
# si = (r*t*amt)/100
# ci = amt*((1+r/100)**t-1)
# print(si)
# print(ci)

# #Convert Kilometer to Miles
# km = float(input())
# fact = 0.621
# miles = km*fact
# print(miles)

# #Convert Clesius to Ffarenheit
# c = float(input())
# f = (c*1.8)+32
# print(f)

#Quadratic Qu
import math
a = int(input())
b = int(input())
c = int(input())
x1 = (-b+math.sqrt((b*b)-(4*a*c)))/2*a
x2 = (-b-math.sqrt((b*b)-(4*a*c)))/2*a
print(x1)
print(x2)