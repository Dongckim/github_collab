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
