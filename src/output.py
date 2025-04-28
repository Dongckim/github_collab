import csv

def save_to_csv(students_data):
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'average'])
        for student in students_data:
            writer.writerow([student['name'], student['average']])
        

