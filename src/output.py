import csv

# express the average grade of each student in the database
def save_to_csv(students_data):
    f = open('../output/result.csv', 'w', newline='') 
    writer = csv.writer(f)
    writer.writerow(['student database'])
    writer.writerow(['name', 'average'])
    for student in students_data:
        writer.writerow([student['name'], student['average']])
    f.close()