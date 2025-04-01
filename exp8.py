#Qn 1 
# with open("input.txt","r")as file1:
#     text = file1.read()
#     with open("output.txt","w") as file2:
#         file2.write(text)

#qn 2
# with open("input.txt","r")as file1:
#     text = file1.read()
#     word = text.split(" ")
#     print(len(word))


#qn 3 
# with open("input.txt","r")as file1:
#     text = file1.read()
#     words = text.split()

#     maxlen = max(len(word) for word in words)
#     max_word = [word for word in words if len(word)==maxlen]

#     print(max_word)


# #Qn 4
# from datetime import datetime
# def log(e):
#     with open("logfole.txt","a")as logfile:
#         timest = datetime.now().strftime("%Y-%m-%d %HH:%MM:%SS")
#         logfile.write(f"{timest}, Error {e}")

# try:
#     1/0
# except Exception as e:
#     log(str(e))


# #Qn 5 

# def add(name,ph,email):
#     with open("contact.txt","a")as c:
#         c.write(f"{name},{ph},{email}\n")
#         print("Added Succesffuly")

# def display():
#     with open("contact.txt","r")as c:
#         text = c.readlines()
#         for word in text:
#             print(word.split(","),"\n")

# def search(name):
#     with open("contact.txt","r")as c:
#         text = c.readlines()
#         found = False
#         for word in text:
#             if name in word:
#                 print(word.split(","))
#                 found = True
#                 break
#     if not found:
#         print("Not fouond")


# add("Hari","962940848","hari@gmail.com")
# add("Harinesh","962940485","harinesh@gmail.com")


# display()

# search("Hari")


# #Qn 7

# def register(name,password):
#     with open("register.txt","a")as r:
#         r.write(f"{name},{password}\n")
#     print("User sign up successfully")

# def login(name,password):
#     with open("register.txt","r")as r:
#         texts = r.readlines()
#         found = False
#         for text in texts:
#             sname,spass = text.strip().split(",")
#             if(sname==name and spass==password):
#                 found = True
#                 print("Login Successfull")
#                 break
#     if not found:
#         print("Login not")

# register("Hari","123")
# login("Hari","123")
# login("Hari","12")        


#Qn 8 
def add(task):
    with open("task.txt","a")as t:
        t.write(f"{task},Pending\n")
    print("Task Added")

def update(task):
    found = False
    with open("task.txt","r")as t:
        texts = t.readlines()

    with open("task.txt","w")as tt:
            for t in texts:
                taskname,tstatus = t.strip().split(",")
                if(taskname==task and tstatus=="Pending"):
                    tt.write(f"{task},Completed\n")
                    found = True
                else:
                    tt.write(f"{taskname},{tstatus}\n")
    
    if found:
        print("Task Updated")
    else:
        print("Task not updated")

def display():
    with open("task.txt","r")as t:
        texts = t.readlines()

        if not texts:
            print("No task")
            return
        else:
            for text in texts:
                print(text.strip())


add("Buy apple")
add("Assign Complete")

display()

update("Buy apple")

display()


