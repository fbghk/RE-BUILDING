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

# 각 연령대의 선호도 계산
age_group_preferences = {}
for group, users in age_groups.items():
    if not users:
        continue  # 회원 정보가 없는 연령대는 건너뜀
    
    # 각 장르의 선호도 카운트 초기화
    genre_count = {}
    for user in users:
        for genre in user.get('preferences', {}).get('like', []):
            genre_count[genre] = genre_count.get(genre, 0) + 1
    
    # 퍼센티지 계산
    total_users = len(users)
    genre_percentages = {
        genre: (count / total_users) * 100
        for genre, count in genre_count.items()
    }
    
    # 연령대별 선호도 저장
    age_group_preferences[group] = genre_percentages

# 결과 출력: 각 연령대의 선호도 비율 표시
for group, preferences in age_group_preferences.items():
    print(f"{group} 선호도:")
    for genre, percentage in sorted(preferences.items(), key=lambda x: -x[1]):
        print(f"  {genre}: {percentage:.1f}%")
