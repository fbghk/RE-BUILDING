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

# y 좌표에 간격을 두기 위한 인덱스 설정
y_positions = range(0, len(genre_names) * 2, 2)  # 2씩 건너뛰어서 간격 확보

# 막대 차트 생성
plt.figure(figsize=(10, 8))
plt.barh(y_positions, genre_percentages, color="skyblue", height=0.6)  # height 조정으로 막대 두께 설정
plt.yticks(y_positions, genre_names)  # y 축 눈금을 장르 이름으로 설정
plt.xlabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값을 각 막대에 표시
for i, value in enumerate(genre_percentages):
    plt.text(value, y_positions[i], f"{value:.1f}%", va="center")

plt.show()
