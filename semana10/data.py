import csv

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
                print(row)
    except FileNotFoundError as ex:
        print("There has not been any file exported, please import data and then you can export")

