FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /collision_bike_info
WORKDIR /collision_bike_info
ADD requirements.txt /collision_bike_info/
RUN pip install -r requirements.txt
ADD . /collision_bike_info/