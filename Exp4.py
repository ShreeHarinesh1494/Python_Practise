# #Qn 1 

# st={}
# print(type(st))
# st={"cement","sand","electronics"}
# print(st)
# st.add("hari")
# print(st)
# st.remove("cement")
# print(st)

# #Qn 2 
# civil = {
#     "cement":"Building",
#     "wood":"Strong",
#     "Nail":"Cutting"
# }

# print(civil)
# print(type(civil))
# print(civil.pop("Nail"))
# print(civil)
# civil["Namae"] = "Hari"
# print(civil)

#Searching

# st={}
# n = int(input())
# for i in range(n):
#     print(f"Student id",{i+1})
#     name = input()
#     rollno = int(input())
#     marks =list(map(float,input().split(" ")))
#     total = sum(marks)
#     avg = total/len(marks)

#     st[rollno]={
#         "Name":name,
#         "Marks":marks,
#         "Total":total,
#         "Avg":avg
#     }


# print("All student details")
# for rollno,details in st.items():
#     print("Roll No",rollno)
#     print("Name",details["Name"])
#     print("Marks",details["Marks"])
#     print("Total",details["Total"])
#     print("Avg",details["Avg"])

# roll = int(input())
# if roll in st:
#     print(f"Roll No",roll)
#     print(f"Name",st[roll]['Name'])
#     print(f"Marks",st[roll]['Marks'])
#     print(f"Total",st[roll]['Total'])
#     print(f"Avg",st[roll]['Avg'])


#Set Operation

s1={"a":1,"b":2,"c":3}
s2={"c":1,"b":2,"a":3}
s11 = s1.keys()
s21 = s2.keys()
print(s11|s21)
print(s11 & s21)
print(s11-s21)
print(s11^s21)
