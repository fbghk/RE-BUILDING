import json
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')

# JSON 파일 불러오기
with open("genre_preferences.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 장르 이름과 퍼센티지 리스트 추출
genre_names = [genre["name"] for genre in data["genres"]]
genre_percentages = [genre["percentage"] for genre in data["genres"]]

# 차트 생성 - 세로 크기를 데이터 개수에 따라 동적으로 조절
plt.figure(figsize=(12, max(8, len(genre_names) * 0.4)))  # 데이터 개수에 따라 세로 크기 조절

# y 위치를 2씩 띄워서 간격 축소 (기존 3에서 2로 변경)
y_positions = range(0, len(genre_names) * 2, 2)

# 가로 막대 차트 생성
plt.barh(y_positions, genre_percentages, color="skyblue", height=0.8)  # height를 0.8로 축소

# y축 레이블 설정 및 폰트 크기 조절
plt.yticks(y_positions, genre_names, fontsize=8)

plt.xlabel("Percentage (%)")
plt.title("Genre Preferences by Percentage")

# 퍼센티지 값 표시
for i, value in zip(y_positions, genre_percentages):
    plt.text(value + (0.01 * max(genre_percentages)), i, 
             f"{value:.1f}%", va="center", fontsize=8)

# 여백 조절
plt.subplots_adjust(left=0.2,    # y축 레이블을 위한 왼쪽 여백
                   right=0.95,   # 오른쪽 여백 축소
                   top=0.95,     # 위쪽 여백 축소
                   bottom=0.05)  # 아래쪽 여백 축소

# tight_layout은 제거하고 위의 subplots_adjust만 사용
plt.show()