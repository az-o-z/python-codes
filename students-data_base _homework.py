print("\n\n\t\t\tHello to the database for the school ! , i used in this code The \"Dictionary and Functions !\" \n\n\n")

newstudent = {} 
students = []
def add():
        while True:
            name = str(input("Enter the name for the student or go to the main menu by typing (return) : "))         
            if(name in newstudent.keys()):
                print("Error 405 | Student already added to the data base please enter a new name ")
            elif (name == "return"):
                 return False         
            else:    
                age = int(input("Enter the age for the student : "))
                bt =str(input("Enter the blood type  for the student : "))
                phonenum = int(input("Enter the phone number for the student : "))
                email = input("Enter the email for the student : ")
                class_number = input("Enter the class number for the student : ")
                grade = float(input("Enter last year grade for the student : "))
                newstudent[name] = {
                        "name" : name,
                        "phone number" : phonenum,
                        "age" : age,
                        "email" : email,
                        "blood type" : bt,
                        "school name" : "Tuwaiq Schools",
                        "class" : "A1-" + class_number,
                        "grade" : grade
                        }
                students.append(name)
                return False
def show():
            if newstudent:
             while True:    
                print("Do you wanna to show all student information or one student or go return to the main menu ? (all/one/return) ")
                ans = input().lower()
                if (ans == "return"):
                    return False
                while(ans == "one"):    
                    print("which student you wanna show information about or go back or return to the main menu (back/return) ?",newstudent.keys())
                    studentcheack = input().lower()
                    if(studentcheack == "back"):
                        break
                    if(studentcheack == "return"):
                        return False
                    if (studentcheack in newstudent):
                     while(True):
                        print("which information do you wana know about",studentcheack,newstudent[studentcheack].keys())
                        info = input("enter the information that you want to know or go back or return to the main menu (back/return) ?  : ")                                
                        if (info in newstudent[studentcheack]):
                            print(studentcheack, info, "is:", newstudent[studentcheack][info])
                        if (info == "back"):
                             break
                        if (info == "return"):
                             return False    
                        else:
                         print("there is not",info,"in the data base",end=" ")
                        while(True):   
                            print("Do you wanna to make another search or back to the main menu ? (con/back)")
                            ans = input().lower()
                            if(ans == "back"):
                                return False
                            if(ans == "con"):
                                break
                            else:
                             print("Error 404 | Invalid input")
                    else:
                        print("there is no studnet with that name please try again :(")                         
                if (ans == "all"):
                    while True:
                        print("names for the students ->",students)
                        print("ages for the students -> ", {name: newstudent[name]["age"] for name in newstudent })
                        print("phone numbers for the students -> ", {name: newstudent[name]["phone number"] for name in newstudent })
                        print("email for the students -> ", {name: newstudent[name]["email"] for name in newstudent })
                        print("blood type for the students -> ", {name: newstudent[name]["blood type"] for name in newstudent })
                        print("class for the students -> ", {name: newstudent[name]["class"] for name in newstudent })
                        print("grade for the students -> ", {name: newstudent[name]["grade"] for name in newstudent })
                        while(True):
                                print("Do you wanna to make print all student information again or return to the main menu ? (con/return)")
                                ans = input().lower()
                                if(ans == "return"):
                                    return False
                                if(ans == "con"):
                                    break
                                else:
                                 print("Error 404 | Invalid input")
                else:
                    print("Error 404 | Invalid input")  
            else:
                print("there is not any registered students yet :(")  
        
def delete():
        if newstudent:
            while (True):
                ans = input("Do you wanna to delete the whole data base or delete a specific user or return to the main menu  ? (all/student/return)")
                if (ans == "return"):
                 return False
                if(ans == "all") : 
                    newstudent.clear()
                    print("all students have been deleted !")
                    return False
                elif(ans == "student"):
                    while True:   
                        print(" which student you wanna delete ? ",newstudent.keys())
                        choice = input().lower()
                        if(choice in newstudent):
                            del newstudent[choice]
                            students.remove(choice)
                            print(choice,"have been deleted !\n\n")
                            choice = input("Do you wanna to delete another student or return to the main menu ? (return/con) ").lower()
                            if(choice == "return"):
                                return False
                            if(choice == "con"):
                                if newstudent:
                                    continue
                                else:
                                    print("there isn't any student to delete in the data base :(")
                                    return False
                            else:
                                print("Error 404 | Invalid input")      
                        else:
                            print(choice,"were not found in the data base please try again") 
                if(ans == "back"):
                    return False        
        else:
             print("there is not any registered students yet :(")  

      
def update():
    if newstudent:
            while True:
                ask = input("Do you wanna to update information for a student or return to the main menu ? (con/return) : ").lower()
                if(ask == "return"):
                    return False  
                if (ask == "con"):
                    while True:     
                        print("which student you wanna update it ?",newstudent.keys())
                        stu = input().lower()
                        while(stu in newstudent):
                            print("what do you wanna update for",stu,newstudent[stu].keys()," or go back or return to the main menu (back/return) ?")
                            update = input().lower()
                            if(update == "back"):
                                break
                            elif(update == "return"):
                                return False
                            elif(update != "name"):
                                while True:
                                    if(update in newstudent[stu]):
                                        print("the current",update,"is",newstudent[stu][update])
                                        change = input("what you wanna change it to ?")
                                        newstudent[stu][update]=change
                                        print(stu,update,"now is ",newstudent[stu][update],"\n\n")
                                        print("Do you wanna to update another thing for",stu,"or return to the main menu (con/return) ?")
                                        ask = input().lower()
                                        if(ask == "con"):
                                            break
                                        elif(ask == "return"):
                                            return False    
                                    else:
                                        print("the",update,"were not found in the data base for",stu,"please try again or return to the main menu(con/return)")    
                                        ask = input().lower()
                                        if (ask == "return"):
                                            return False
                                        if(ask == "con"):
                                            break
                                        else:
                                            print("Error 404 | Invalid input")
                            if (update == "name"):
                                while True :
                                    print("Erorr 406 | you cannot change the name for",stu,"plaese delete it from the data base then make another one with the new name ")
                                    print("Do you wanna to return or make another update for",stu," (return/con)?")
                                    ask = input().lower()
                                    if(ask == "return"):
                                        return False
                                    if (ask == "con"):
                                        break
                                    else:
                                        print("Error 404 | Invalid input")
                            else:
                                print("the",update,"were not found in the data base please try again") 
                                
                        else:
                            print(stu,"were not found in the data base please try again")
                else:
                    print("Error 404 | Invalid input")           
    else:
         print("there is not any registered students yet :(")            

while (True):
    print("Do you wanna add a new student to the database or show a registred ones or delete or upadte or exit ? (Show/Add/exit/del/update)",end="")
    ans = input().lower()
    if (ans != "show" and ans !="add" and ans !="exit" and ans !="del" and ans !="update" ):
            print("Error 404 | Invalid input")
            ans = input("Do you wanna add a new student to the database or show a registred ones or delete or upadte or exit ? (Show/Add/exit/del/update)").lower()
    if (ans == "add"):
        add()
    if(ans == "show"):
        show()   
    elif(ans == "del"):
       delete()
    elif(ans == "update"):
     update()
    elif(ans == "exit"):
      print("See you later ^-^")
      break            

    """ 
    this code was written by Abdulaziz Almarshed ^_^
    
    
    edit it at 24 nov | adding in delete a while loop to make sure the user enter a valid input | use functions ^_^ 
    
    """

