import json
from collections import defaultdict

# JSON 파일 로드
with open('movie-information.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 장르별 선호도 및 비선호도 카운트 초기화
genre_counts = defaultdict(int)
hate_genre_counts = defaultdict(int)

# 유저별 선호도 및 비선호도 카운트
for user in data['users']:
    if user.get('age') is None:  # 비회원이면 건너뛰기
        continue
    
    # 선호 장르 카운트
    for genre in user.get('preferences', {}).get('like', []):
        genre_counts[genre] += 1
    
    # 비선호 장르 카운트
    for genre in user.get('preferences', {}).get('hate', []):
        hate_genre_counts[genre] += 1

# 결과 출력
print("장르별 선호도:")
for genre, count in genre_counts.items():
    print(f'"{genre}" {count}개')

print("\n장르별 비선호도:")
for genre, count in hate_genre_counts.items():
    print(f'"{genre}" {count}개')
