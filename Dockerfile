# 1. 베이스 이미지 설정
FROM python:3.8

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY . .

# 5. 컨테이너에서 실행할 기본 명령
CMD ["python", "app.py"]
