import json
from collections import Counter

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

# 연령대 그룹화
for user in data['users']:
    age = user.get('age')
    if age is None:
        non_members += 1
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

# 연령대별 선호 장르 퍼센티지 계산
age_group_preferences = {}

for group, users in age_groups.items():
    if not users:
        age_group_preferences[group] = "회원 없음"
        continue

    # 모든 선호 장르 수집
    likes = []
    for user in users:
        likes.extend(user['preferences'].get('like', []))  # 선호 장르 목록 추가

    # 장르별 카운트 계산
    genre_counts = Counter(likes)
    total_likes = sum(genre_counts.values())

    # 퍼센티지로 변환
    genre_percentages = {genre: (count / total_likes) * 100 for genre, count in genre_counts.items()}
    
    # 내림차순 정렬
    sorted_genre_percentages = dict(sorted(genre_percentages.items(), key=lambda item: item[1], reverse=True))

    # 결과 저장
    age_group_preferences[group] = sorted_genre_percentages

# 결과 출력: 연령대별 선호도
for group, preferences in age_group_preferences.items():
    print(f"{group} 선호도:")
    if preferences == "회원 없음":
        print("  - 회원 없음")
    else:
        for genre, percentage in preferences.items():
            print(f"  {genre}: {percentage:.1f}%")
    print()
