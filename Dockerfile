FROM python:latest

WORKDIR /myproject

ADD hello.py /myproject

RUN pip install Flask

RUN pip install pendulum

CMD ["flask","--app","hello","run","--host=0.0.0.0"]
