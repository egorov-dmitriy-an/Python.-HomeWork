import csv
def find_progress(file_temp, id):
    with open(file_temp, encoding='UTF-8') as r_file:
        file = list(csv.reader(r_file, delimiter=','))
        print('-----------------------------------------')
        for row in file:
            if id == row[0]:
                print(row[1], row[2])
        print('-----------------------------------------')