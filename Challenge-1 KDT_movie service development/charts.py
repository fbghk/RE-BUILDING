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

# x 위치를 2씩 띄워서 막대 사이 간격 확보
x_positions = range(0, len(genre_names) * 2, 2)

# 세로 막대 차트 생성
plt.figure(figsize=(12, 8))  # 차트 크기 조정
plt.bar(x_positions, genre_percentages, color="skyblue", width=1.5)  # width로 막대 두께 조정
plt.xticks(x_positions, genre_names, rotation=90)  # x축 레이블 설정 및 회전
plt.ylabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값을 각 막대 위에 표시
for i, value in zip(x_positions, genre_percentages):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center", va="bottom")

plt.tight_layout()  # 차트 요소가 겹치지 않도록 자동 조정
plt.show()
