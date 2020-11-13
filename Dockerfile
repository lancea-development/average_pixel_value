FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY docker-entrypoint.sh /code/
RUN pip install -r requirements.txt
COPY avg_pixel_value /code/