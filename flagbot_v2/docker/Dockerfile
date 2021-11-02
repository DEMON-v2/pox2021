FROM gorialis/discord.py

MAINTAINER jhyeon "stjhyeon@kakao.com"

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "run.py"]