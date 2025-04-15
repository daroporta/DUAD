import csv
from lists import create_list

def export_data(file_path, data, headers):
    try:
        with open(file_path, "w", encoding="utf-8") as file: 
            writer=csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as ex:
        print("There was an error exporting the data")


def import_file(file_path, list_of_income_and_expenses):
    list_of_categories, list_of_income_and_expenses= create_list()
    with open(file_path, "r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            list_of_income_and_expenses.append(row)   
        return list_of_income_and_expenses    
    

def export_data_of_categories(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8") as file: 
        writer=csv.writer(file)
        writer.writerow(headers)
        for category in data:
            writer.writerow([category])


def import_file_categories(file_path, list_of_categories):
    list_of_categories, list_of_income_and_expenses= create_list()
    with open(file_path, "r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            list_of_categories.append(row)   
        return list_of_categories