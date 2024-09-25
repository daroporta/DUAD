import csv
from actions import Student


def export_data(file_path, data):
    
    with open(file_path, "w", encoding="utf-8") as file:  
        writer=csv.DictWriter(file, fieldnames= ["Name", "Class_group", "Spanish", "English", "History", "Science", "Average"])
        writer.writeheader()
        for student in data:
            writer.writerow(student.convert_dictionary())


def import_file(file_path):
    try:
        with open(file_path, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                student = Student.dict_to_object(row)  #creates the object from the dictionary (instance)
                import_list() .append(student) #adds the object to the list
                student.print_data() 
    except FileNotFoundError as ex:
        print("There has not been any file exported, please export data and then you can import")

def import_list():
    from Menu import students_list
    return students_list