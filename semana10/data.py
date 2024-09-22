import csv
# por que no me permitia usar el from Menu import student_list?  me daba un error de que la informacion estaba como en circulacion y no me dejaba ejecutar el codigo. 
def export_data(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8") as file:   #should the option be append or write?
        writer=csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def import_file(file_path):
    try:
        with open(file_path, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                import_list().append(row)    #FIX ERROR 
                print(row)
    except FileNotFoundError as ex:
        print("There has not been any file exported, please import data and then you can export")

def import_list():
    from Menu import students_list
    return students_list
