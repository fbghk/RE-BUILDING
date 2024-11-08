import json
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # 'Malgun Gothic'이 설치된 경우

# JSON 파일 불러오기
with open("genre_preferences.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 장르 이름과 퍼센티지 리스트 추출
genre_names = [genre["name"] for genre in data["genres"]]
genre_percentages = [genre["percentage"] for genre in data["genres"]]

# 세로 막대 차트 생성
plt.figure(figsize=(12, 8))  # 차트 크기 조정
plt.bar(genre_names, genre_percentages, color="skyblue")
plt.xticks(rotation=90)  # x축의 글자를 90도 회전
plt.ylabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값을 각 막대 위에 표시
for i, value in enumerate(genre_percentages):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center", va="bottom")

plt.tight_layout()  # 차트 요소가 겹치지 않도록 자동 조정
plt.show()
