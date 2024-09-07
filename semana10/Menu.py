import actions, data 

def select_option():
    while True:
        print("\n",5*("*"),"Academic system",5*("*"),"\n")
        print("1. Add student´s information")
        print("2. Information of each student")
        print("3. Top 3 best average scores")
        print("4. General group average score")
        print("5. Export the data to an CSV file")
        print("6. Import the saved data from the CSV file")
        print("7. Exit\n")

        try:
            option=int(input("Please type the option you want to execute: "))
            if option == 1:
                actions.add_student(students_list)
            elif option == 2:
                actions.check_student(students_list)
            elif  option == 3:
                actions.calculate_top_averages(students_list)
            elif  option == 4:
                actions.calculate_total_averages(students_list)
            elif  option == 5:
                try:
                    data.export_data("Student_information", students_list, students_list[0].keys())
                except IndexError:
                    print("You have not added any student to export. Please add a student.") 
            elif  option == 6:
                data.import_file("Student_information")    
            elif  option == 7:
                print("\nThank you for visiting our Academic system\n\nGood bye...")
                break
            else:
                print("The option you have selected is not valid, please select between 1 and 7")
        except ValueError:
            print("The value you have entered is not valid, please try again")

students_list=[]
