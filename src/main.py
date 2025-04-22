# 이 파일은 건드리지 마세요!
# 제대로 작동하는지 확인하는 파일입니다.

import json
from validate import validate_json
from sort import sort_students
from average import calculate_average
from output import save_to_csv

json_file = 'data/newLambdaComers.json'

def main():
    try:
        # 1. 기본 세팅/JSON 파일 열기 - 동찬
        with open(json_file, 'r') as f:
            students_data = json.load(f)

        # 2. JSON 검증 - 범준
        validate_json(students_data)

        # 3. 학생들 이름 기준으로 정렬 - 성빈
        students_data = sort_students(students_data)

        # 4. 평균 점수 계산 - 희아
        for student in students_data:
            student['average'] = calculate_average(student['scores'])

        # 5. 결과를 CSV로 저장 - 민서
        save_to_csv(students_data)

        print("200")

    except Exception as e:
        print("400")
        print(f"Error Occurred: {e}")

if __name__ == "__main__":
    main()