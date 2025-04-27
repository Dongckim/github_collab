import json
import os

# Build the correct file path to your JSON file
json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'newLambdaComers.json')

# Open the JSON file with UTF-8 encoding
with open(json_file_path, encoding='utf-8') as file:
    data = json.load(file)

# Initialize variables
total_score = 0
student_count = 0  # We will count students who have valid scores

# Loop through each student
for student in data:
    # Check if the 'scores' key contains a valid list of numbers
    if isinstance(student['scores'], list) and all(isinstance(score, (int, float)) for score in student['scores']):
        # Calculate the sum of scores for the student
        total_score += sum(student['scores'])  # Add the sum of the student's scores to total
        student_count += 1  # Increment the count of students with valid scores

# Calculate the average score if there are any valid students
if student_count > 0:
    average_score = total_score / student_count
    print(f"Average Score: {average_score:.2f}")
else:
    print("No valid students with scores.")
