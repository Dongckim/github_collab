def get_name(student):
    return student['name']

def sort_students(students_data):

    sorted_data = sorted(students_data, key=get_name)
    return sorted_data