# JSON PARSER 협업 프로젝트
이 프로젝트는 JSON 데이터를 처리하는 여러 기능을 나누어 작업하는 협업 연습 프로젝트입니다.

## 실행 방법
1. `pip install -r requirements.txt` 로 필요한 패키지 설치
2. `python src/main.py` 실행

## 브랜치 작업 안내
- 각자의 기능으로 브랜치 이름을 만들고, 해당 브랜치에서 기능을 구현한 후, PR을 생성해 주세요.
- 각 기능은 별도의 파일로 작성됩니다: `validate.py`, `sort.py`, `average.py`, `output.py`
- **Develop** 브랜치에 PR 날려주시면 됩니다.

**[참고자료 - 람다플릭스](https://lambda-flix.com/github-collab/)**

## Git Convention
- [협업을 위한 git 컨벤션 - Google](https://developers.google.com/blockly/guides/contribute/get-started/commits)
- [협업을 위한 Pull Request 컨벤션 - Google](https://developers.google.com/blockly/guides/contribute/get-started/write_a_good_pr?_gl=1*284er9*_up*MQ..*_ga*NzYzMzUxODQzLjE3NDUzNDA0Mzg.*_ga_R5G2Y6GLVC*MTc0NTM0MDQzNy4xLjEuMTc0NTM0MDQzNy4wLjAuMA..)
- [브랜치 전략](https://aliencoder.tistory.com/79)꼭 참고해주세요.
- 제가 미리 해두었으니, 참고해도 됩니다.

## 역할분배
### 1. 기본 세팅/JSON 파일 열기 - 동찬
### 2. JSON 검증 - 범준 (validate.py)
### 3. 학생들 이름 기준으로 정렬 - 성빈 (sort.py)
### 4. 평균 점수 계산 - 희아 (average.py)
### 5. 결과를 CSV로 저장 - 민서 (output.py)