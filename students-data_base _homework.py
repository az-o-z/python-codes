print("\n\n\t\t\tHello to the database for the school ! , i used in this code The \"Dictionary\" \n\n\n")

newstudent = {}
students = []
while (True):
    print("Do you wanna add a new student to the database or show a registred ones or delete or upadte or exit ? (Show/Add/exit/del/update)",end="")
    ans = input().lower()
    if (ans != "show" and ans !="add" and ans !="exit" and ans !="del" and ans !="update" ):
            print("Error 404 | Invalid input")
            ans = input("Do you wanna add a new student to the database or show a registred ones or delete or upadte or exit ? (Show/Add/exit/del/update)").lower()
    if (ans == "add"):
            name = str(input("Enter the name for the student : "))         
            if(name in newstudent.keys()):
                print("Error 405 | Student already addded to the data base please enter a new name")
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
    if(ans == "show"):
           if newstudent:
            print("Do you wanna to show all student information or one student ? (all/one)")
            ans = input().lower()
            while (ans != "all" and ans != "one"):
                    print("Error 404 | Invalid input")
                    break
            if(ans == "one"):    
             print("which student you wanna show information about ?",newstudent.keys())
             studentcheack = input().lower()
             while (studentcheack in newstudent):
              print("which information do you wana know about",studentcheack,newstudent[studentcheack].keys())
              info = input("enter the information that you want to know ? : ")                                
              if (info in newstudent[studentcheack]):
                print(studentcheack, info, "is:", newstudent[studentcheack][info])
              else:
               print("there is not",info,"in the data base",end=" ")  
              print("Do you wanna to make another search or back to the main menu ? (con/back)")
              ans = input().lower()
              while(ans != "con" and ans != "back"):
                    print("Error 404 | Invalid input")
                    print("Do you wanna to make another search or back to the main menu ? (con/back)")
                    ans = input().lower()
                    
              if(ans == "back"):
                    
                    break
              if(ans == "con"):
                    True                                 
             else:
              print("there is no studnet with that name please try again :(")                         
            if( ans == "all"):
             print("names for the students ->",students)
             print("ages for the students -> ", {name: newstudent[name]["age"] for name in newstudent })
             print("phone numbers for the students -> ", {name: newstudent[name]["phone number"] for name in newstudent })
             print("email for the students -> ", {name: newstudent[name]["email"] for name in newstudent })
             print("blood type for the students -> ", {name: newstudent[name]["blood type"] for name in newstudent })
             print("class for the students -> ", {name: newstudent[name]["class"] for name in newstudent })
             print("grade for the students -> ", {name: newstudent[name]["grade"] for name in newstudent })

           else:
            print("there is not any registered students yet :(")  
                      
    
    
    elif(ans == "del"):
        if newstudent:
            ans = input("Do you wanna to delete the whole data base or delete a specific user ? (all/student)")
            if(ans != "all" and ans !="student"):
                print("Error 404 | Invalid input")
            if(ans == "all") : 
                newstudent.clear()
                print("all students have been deleted !")
            while(ans == "student"):   
                print(" which student you wanna delete ? ",newstudent.keys())
                choice = input().lower()
                if(choice in newstudent):
                    del newstudent[choice]
                    students.remove(choice)
                    print(choice,"have been deleted !")
                    break
                else:
                    print(choice,"were not found in the data base please try again") 
        else:
             print("there is not any registered students yet :(")  


    elif(ans == "update"):
        while newstudent:
                ans = input("Do you wanna to update information for a student or back to the main menu ? (con/back) : ").lower()
                if (ans != "con" and ans != "back"):
                    print("Error 404 | Invalid input")
                    ans = input("Do you wanna to update information for a student or back to the main menu ? (con/back) : ").lower()
                if (ans == "con"):    
                    print("which student you wanna update it ?",newstudent.keys())
                    ans = input().lower()
                    if(ans in newstudent):
                        print("what do you wanna update for",ans,newstudent[ans].keys())
                        update = input().lower()
                        while(update != "name"):
                            if(update in newstudent[ans]):
                                print("the current",update,"is",newstudent[ans][update])
                                change = input("what you wanna change it to ?")
                                newstudent[ans][update]=change
                                break
                            else:
                                print("the",update,"were not found in the data base please try again")
                                break    
                        if(update in newstudent[ans]):  
                            print("Erorr 406 | you cannot change the name for",ans,"plaese delete it from the data base then make another one with the new name ")
                            
                    else:
                            print(ans,"were not found in the data base please try again")
                if(ans == "back"):
                    break             
        else:
             print("there is not any registered students yet :(")            

    elif(ans == "exit"):
      print("See you later ^-^")
      break            

    # this code was written by Abdulaziz Almarshed ^_^
