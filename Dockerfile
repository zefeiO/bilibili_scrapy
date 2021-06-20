FROM python:3.8

ADD config.py .
ADD fetch_comments.py .
ADD main.py .
ADD videos.py .

RUN pip install requests

CMD ["python", "./main.py"]