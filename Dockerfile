FROM python:3.9

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y dos2unix

RUN dos2unix /app/crawler.sh

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/crawler.sh

ENTRYPOINT ["bash", "/app/crawler.sh"]