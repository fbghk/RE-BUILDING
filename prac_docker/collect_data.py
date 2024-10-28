import requests
import pandas as pd

def fetch_kbo_team_stats():
    # 가상의 URL (실제 API가 있다면 해당 URL을 사용)
    url = "https://www.koreabaseball.com/Record/Team/Defense/Basic.aspx"
    response = requests.get(url)
    data = response.json()

    # 데이터를 pandas 데이터프레임으로 변환
    df = pd.DataFrame(data)
    df.to_csv("/data/team_stats.csv", index=False)
    print("KBO 팀 통계 데이터를 성공적으로 저장했습니다.")

fetch_kbo_team_stats()
