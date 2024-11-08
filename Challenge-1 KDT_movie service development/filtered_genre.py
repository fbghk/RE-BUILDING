import json
from collections import defaultdict

# JSON 파일 로드
with open('movie-information.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 장르별 선호도 및 비선호도 카운트 초기화
genre_counts = defaultdict(int)
hate_genre_counts = defaultdict(int)

# 유저별 선호도 및 비선호도 카운트
total_users = 0  # 전체 유저 수

for user in data['users']:
    if user.get('age') is None:  # 비회원이면 건너뛰기
        continue
    
    total_users += 1  # 유효한 유저 수 증가
    
    # 선호 장르 카운트
    for genre in user.get('preferences', {}).get('like', []):
        genre_counts[genre] += 1
    
    # 비선호 장르 카운트
    for genre in user.get('preferences', {}).get('hate', []):
        hate_genre_counts[genre] += 1

# 선호도 퍼센트 계산 후 정렬
sorted_genre_counts = sorted(genre_counts.items(), key=lambda x: (x[1] / total_users) * 100, reverse=True)

# 비선호도 퍼센트 계산 후 정렬
sorted_hate_genre_counts = sorted(hate_genre_counts.items(), key=lambda x: (x[1] / total_users) * 100, reverse=True)

# 결과 출력 (선호도)
print("장르별 선호도:")
for genre, count in sorted_genre_counts:
    percentage = (count / total_users) * 100  # 퍼센트 계산
    print(f'"{genre}" {count}개 ({percentage:.2f}%)')

# 결과 출력 (비선호도)
print("\n장르별 비선호도:")
for genre, count in sorted_hate_genre_counts:
    percentage = (count / total_users) * 100  # 퍼센트 계산
    print(f'"{genre}" {count}개 ({percentage:.2f}%)')

genre_names = [genre for genre, count in sorted_genre_counts]
genre_percentages = [(count / total_users) * 100 for genre, count in sorted_genre_counts]

# 선호도 데이터를 딕셔너리 형식으로 준비
genre_data = {
    "genres": [{"name": genre, "percentage": percentage} for genre, percentage in zip(genre_names, genre_percentages)]
}

# JSON 파일로 저장
with open("genre_preferences.json", "w", encoding="utf-8") as file:
    json.dump(genre_data, file, ensure_ascii=False, indent=4)

print("데이터가 genre_preferences.json 파일로 저장되었습니다.")