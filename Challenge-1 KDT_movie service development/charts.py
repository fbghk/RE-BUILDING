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

# y 위치를 3씩 띄워서 막대 사이 간격 확보
y_positions = range(0, len(genre_names) * 3, 3)

# 가로 막대 차트 생성
plt.figure(figsize=(12, 8))  # 차트 크기 조정
plt.barh(y_positions, genre_percentages, color="skyblue", height=1.5)  # height로 막대 두께 조정
plt.yticks(y_positions, genre_names)  # y축 레이블 설정
plt.xlabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값을 각 막대 옆에 표시 (글꼴 크기 조정)
for i, value in zip(y_positions, genre_percentages):
    plt.text(value + (0.01 * max(genre_percentages)), i, f"{value:.1f}%", va="center", fontsize=6.5)  # fontsize 6.5로 줄임

# 여백을 줄여서 차트 틀과 막대 사이의 빈칸 없애기
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.tight_layout()  # 차트 요소가 겹치지 않도록 자동 조정
plt.show()
