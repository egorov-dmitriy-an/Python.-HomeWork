import csv

def find_parent(file_temp, id):
    with open(file_temp, encoding='UTF-8') as r_file:
        file = list(csv.reader(r_file, delimiter=','))
        print('-----------------------------------------')
        print(file[0][1], file[0][2], file[0][3], file[0][4])
        for row in file:
            if id == row[0]:
                print(row[1], row[2], row[3], row[4])
        print('-----------------------------------------')