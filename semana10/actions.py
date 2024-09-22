
def add_student(students_list):
    while True:
        try:
            add=input("\nDo you want to add a student\n(Yes or No)?: ").upper()
            if add == "YES":
                student={                                        
                        "name": input("\nName of student: "),
                        "class_group": input("\nInsert the Class group ID ?: ")}
                try:
                    while True:                                                   
                        Spanish=float(input("Spanish score: " )) 
                        if 0 <= Spanish <= 100:
                            student["Spanish_score"]=Spanish
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        English=float(input("English score: ")) 
                        if 0 <= English <= 100:
                            student["English_score"]=English
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        History=float(input("History score: "))
                        if 0 <= History <= 100:
                            student["History_score"]=History
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        Science=float(input("Science score: "))
                        if 0 <= Science <= 100:
                            student["Science_score"]=Science
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    students_list.append(student)
                except Exception as ex:
                    print(f"Please type a valid score between 0 and 100, error found: {ex}")
                for student in students_list:
                            average=(float(student["Spanish_score"]) + float(student["English_score"]) + float(student["History_score"]) + float(student["Science_score"])) / 4   # why does it not work like this, if the subject is float? 
                            student["average"]=average
            elif add=="NO":
                break
            else:
                print("Invalid value. Please type Yes or No.")
        except ValueError:
            print("The value you have entered is not valid, please type Yes or No")


def check_student(student_list):
    for student in student_list:
        print(student)


def calculate_top_averages(student_list):
    highest_average=sorted(student_list, key=lambda x: x["average"], reverse=True)   # si no cambiaba a float el average me daba error en lambda el parametro. 
    tops=highest_average[:3]
    print("The highest average scores are:")
    for students in tops:
        print(f"Name: {students['name']}, Average:{students['average']}")


def calculate_total_averages(student_list):
    total_average=0
    for student in student_list:
        total_average=float(student['average']) + total_average
    total= total_average / len(student_list)
    print(f"The total average of all the students is: {total}")


