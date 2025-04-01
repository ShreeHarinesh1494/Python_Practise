# #Qn book
# book=[]
# ch='y'
# while(ch=='y'):
#     print(''''
#     '1.append book name'
#     '2.remove book'
#     '3.print book details'
#     ''')

#     choice = int(input())
#     if(choice==1):
#         name = input()
#         book.append(name)
#     elif(choice==2):
#         rem = input()
#         book.remove(rem)
#     elif(choice==3):
#         for i in book:
#             print(i)
#     else:
#         ch=input("Wrong input do you need tp cpntine")
#         if(ch!='y'):
#             print("Tahnk you")


#Qn tuple

tup1 = ("cement","wood","sand")
tup2 = ("water","nail","screw driver")
ch='y'
while(ch=='y'):
    print(''''
    '1.append construciton name'
    '2.remove construction'
    '3.print construction details'
    ''')

    choice = int(input())
    if(choice==1):
        print(tup1)
    elif(choice==2):
        print(tup2)
    elif(choice==3):
        print(len(tup1)+len(tup2))
    else:
        ch=input("Wrong input do you need tp cpntine")
        if(ch!='y'):
            print("Tahnk you")