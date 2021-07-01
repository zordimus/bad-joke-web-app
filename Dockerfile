# syntax=docker/dockerfile:1
#
# docker run -d -p 5000:5000 python-docker

FROM python:3.8-slim-buster

WORKDIR /app

#Installs required tools
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#Copy source codes
COPY /src/ .
COPY /file/ ./file/

CMD [ "python3", "src/main.py", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]