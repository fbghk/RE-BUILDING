# Python 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 스크립트 복사
COPY collect_data.py .

# 데이터를 저장할 볼륨 생성
VOLUME /data

# 스크립트 실행
CMD ["python", "collect_data.py"]
