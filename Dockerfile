FROM python:3.7-alpine
RUN apk update
WORKDIR /iplwinners
ADD . /iplwinners
RUN pip install -r requirements.txt
CMD ["python3","app.py"]