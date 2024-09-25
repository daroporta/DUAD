class Student:
    def __init__(self, name, class_group, Spanish, English, History, Science, Average): #constructor
        self.name=name
        self.class_group=class_group
        self.Spanish=Spanish
        self.English=English
        self.History=History
        self.Science=Science
        self.Average=Average
    

    def get_average(self): #getter for average
        return self.Average


    def get_name(self):#getter
        return self.name


    def print_data(self):
        print(f"Name {self.name}, class-ID {self.class_group}, Spanish score {self.Spanish}, English score {self.English}, History score {self.History}, Science score {self.Science}, Average {self.Average}")


    def convert_dictionary(self): 
        return {"Name": self.name,
                "Class_group": self.class_group,
                "Spanish": self.Spanish, 
                "English": self.English, 
                "History": self.History,
                "Science": self.Science,
                "Average": self.Average}


    @classmethod     #used a decorator, which was the easiest way I found to convert from obj to dic
    def dict_to_object(cls, data): #csl special parameter to represent the class, data = dict
        return cls(
            name=data["Name"],
            class_group=data["Class_group"],
            Spanish=float(data["Spanish"]),
            English=float(data["English"]),
            History=float(data["History"]),
            Science=float(data["Science"]),
            Average=float(data["Average"])
        )


def add_student(students_list):
    while True:
        try:
            add=input("\nDo you want to add a student\n(Yes or No)?: ").upper()
            if add == "YES":                                 
                name= input("\nName of student: ")
                class_group=input("\nInsert the Class group ID ?: ")
                try: 
                    while True:                                                   
                        Spanish=float(input("Spanish score: " )) 
                        if 0 <= Spanish <= 100:
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        English=float(input("English score: ")) 
                        if 0 <= English <= 100:
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        History=float(input("History score: "))
                        if 0 <= History <= 100:
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    while True: 
                        Science=float(input("Science score: "))
                        if 0 <= Science <= 100:
                            break
                        else:
                            print("Please type a valid score between 0 and 100")
                    Average= (Spanish + English + History + Science ) / 4

                    student = Student(name, class_group, Spanish, English, History, Science, Average)
                    students_list.append(student)
                except Exception as ex:  
                    print(f"Please type a valid score between 0 and 100, error found: {ex}")
            elif add=="NO":
                break
            else:
                print("Invalid value. Please type Yes or No.")
        except ValueError:
            print("The value you have entered is not valid, please type Yes or No")


def check_student(student_list):
    for student in student_list:
        student.print_data()


def calculate_top_averages(student_list):
    highest_average=sorted(student_list, key=lambda x: x.get_average(), reverse=True)
    tops=highest_average[:3]
    print("The highest average scores are:")
    for student in tops:
        print(f"Name: {student.get_name()}, Average:{student.get_average()}")


def calculate_total_averages(student_list):
    total_average=0
    for student in student_list:
        total_average=float(student.get_average()) + total_average
    total= total_average / len(student_list)
    print(f"The total average of all the students is: {total}")