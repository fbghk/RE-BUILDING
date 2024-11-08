import json

# JSON 파일 로드
with open('movie-information.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 세분화된 연령대별 그룹 초기화
age_groups = {
    '10대 후반': [],
    '20대 초반': [],
    '20대 중반': [],
    '20대 후반': [],
    '30대 초반': [],
    '30대 중반': [],
    '30대 후반': [],
    '40대 초반': [],
    '40대 중반': [],
    '40대 후반': [],
    '50대 초반': [],
    '50대 중반': [],
    '50대 후반': []
}

# 비회원 카운트 변수
non_members = 0

# 연령대 그룹화 함수
for user in data['users']:
    age = user.get('age')  # 'age'가 없으면 None 반환
    if age is None:
        non_members += 1  # 비회원 수 증가
        continue  # 비회원이므로 다음 사용자로 넘어감
    

    # 연령대 분류
    if 17 <= age <= 19:
        age_groups['10대 후반'].append(user)
    elif 20 <= age <= 23:
        age_groups['20대 초반'].append(user)
    elif 24 <= age <= 26:
        age_groups['20대 중반'].append(user)
    elif 27 <= age <= 29:
        age_groups['20대 후반'].append(user)
    elif 30 <= age <= 33:
        age_groups['30대 초반'].append(user)
    elif 34 <= age <= 36:
        age_groups['30대 중반'].append(user)
    elif 37 <= age <= 39:
        age_groups['30대 후반'].append(user)
    elif 40 <= age <= 43:
        age_groups['40대 초반'].append(user)
    elif 44 <= age <= 46:
        age_groups['40대 중반'].append(user)
    elif 47 <= age <= 49:
        age_groups['40대 후반'].append(user)
    elif 50 <= age <= 53:
        age_groups['50대 초반'].append(user)
    elif 54 <= age <= 56:
        age_groups['50대 중반'].append(user)
    elif 57 <= age <= 59:
        age_groups['50대 후반'].append(user)


# 결과 출력: 각 연령대의 회원 수 표시
age_group_counts = {group: len(users) for group, users in age_groups.items()}
age_group_counts['비회원'] = non_members  # 비회원 수 추가
print(age_group_counts)
