import csv

def save_to_csv(students_data):
    f = open('output.csv', 'w', newline='') 
    writer = csv.writer(f)
    writer.writerow(['name', 'average'])
    for student in students_data:
        writer.writerow([student['name'], student['average']])
    f.close()

