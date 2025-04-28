# import json
# import os
# current_dir = os.path.dirname(__file__)
# json_file_path = os.path.join(current_dir, '..', 'data', 'newLambdaComers.json')
#
# # Normalize the path
# json_file_path = os.path.abspath(json_file_path)
#
# # Load the JSON
# with open(json_file_path, 'r', encoding='utf-8') as f:
#     students = json.load(f)
def validate_json(students_data):
    for member in students_data:
        name = member.get('name')
        scores = member.get('scores')

        if not isinstance(name, str):
            print(f"Invalid student name type for {member}")
        if not isinstance(scores, list):
            print(f"Invalid scores format for {name}: current format {type(scores)}")
        for score in scores:
            if not isinstance(score, int):
                print(f"Invalid score types for {name}")
                break
        if not scores:
            print(f"Scores for {name} is not available")

# validate_json(students)