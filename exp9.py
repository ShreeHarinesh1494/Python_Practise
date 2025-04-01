
# #Qn 1 
# a = int(input())
# b = int(input())

# try:
#     div = a/b
#     print(div)
# except ZeroDivisionError:
#     print("divide by zero")
# except ValueError:
#     print("Integer only")


#Qn 2 
# age = int(input())
# try:   
#     if(age>=18):
#         print("You are allowed to vote")
#     else:
#         print("Not allowed")

# except ValueError:
#     print("Integer value only")


# #Qn 3 
# def ranges(a,b):
#     try:
#         while True:
#             marks = int(input())
#             if(a<=marks<=b):
#                 print(marks)
#                 break
#             else:
#                 print("Out of range")
#     except ValueError:
#         print("Integer value")

# ranges(1,100)


# #Qn 4 
# try:
#     with open("input.txt","r")as input_file:
#         text = input_file.read()
#         print("File Content")
#         print(text)
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission Error")
# except Exception as e:
#     print(f"Error Occured {e}")


# #Qn 5

# class AcntException(Exception):
#     pass

# def withdraw(amt,bal):
#     try:
#         if(amt>bal):
#             raise AcntException("Blanace is less")
#         elif(amt<=0):
#             raise AcntException("Amt must to greater than 0")
#         elif(amt<bal):
#             bal-=amt
#             print("Withdraw Successfull")
#     except AcntException as e:
#         print(f"Error {e}")
#     except ValueError:
#         print("Enter Integer")

# bal = 5000
# withdraw(6000,bal)
# withdraw(-100,bal)
# withdraw(2000,bal)


# #Qn 6
# class Ageerror(Exception):
#     pass
# def register():
#     try:
#         age = int(input())
#         if(age<18 or age>100):
#             raise Ageerror("Age is not proper")
#         print("Successfully Registred")
#     except Ageerror as e:
#         print(f"Error {e}")
#     except ValueError:
#         print("Integer Only")

# register()


#Qn 7 
class Qnerror(Exception):
    pass

class pnerror(Exception):
    pass

def add(inv,prod,qn):
    try:
        if(qn<=0):
            raise Qnerror("Invalid Quantity")
        else:
            inv[prod] = inv.get(prod,0)+qn
            print(f"Added {qn} of {prod}")
    except Qnerror as e:
        print(f"Erorr {e}")

def remove(inv,prod,qn):
    try:
        if prod not in inv:
            raise pnerror("Product Not Found")
        elif(inv[prod]<qn):
            raise Qnerror("Not enough stock")
        else:
            inv[prod]-=qn
            print(f"Quantity of {prod} is {qn}")
    except Qnerror as e:
        print(f"Error {e}")
    except pnerror as e:
        print(f"Error {e}")

def display(inv):
    print("Inventory Items")
    if not inv:
        print("Inventory is empty")
    else:
        for prod,qn in inv.items():
            print(f"{prod} , {qn}")
    
    
inv = {}
add(inv,"bread",5)
add(inv,"computer",10)
add(inv,"water",0)

display(inv)

remove(inv,"bread",3)
remove(inv,"computer",2)

display(inv)

    
