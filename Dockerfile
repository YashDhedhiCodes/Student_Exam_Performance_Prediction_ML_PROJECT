FROM python:3.12.7-slim-buster
WORKDIR /application
COPY . /application 

RUN apt update -y && apt insatll awscli -y
RUN pip install -r requirements.txt
CMD ["python","application.py"]