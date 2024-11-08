import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # 'Malgun Gothic'이 설치된 경우

# JSON 파일 불러오기
with open("genre_preferences.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 장르 이름과 퍼센티지 리스트 추출
genre_names = [genre["name"] for genre in data["genres"]]
genre_percentages = [genre["percentage"] for genre in data["genres"]]

# 막대 차트 생성
plt.figure(figsize=(10, 6))
plt.barh(genre_names, genre_percentages, color="skyblue")
plt.xlabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값을 각 막대에 표시
for index, value in enumerate(genre_percentages):
    plt.text(value, index, f"{value:.1f}%", va="center")

plt.show()
