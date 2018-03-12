FROM python:3.6.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./requirements/locked.txt /code/
RUN pip install -r locked.txt
ADD . /code/
