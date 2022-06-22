FROM python:3.10-slim


WORKDIR /code
COPY requirements.txt .
RUN pip3 install -t requirements.txt
COPY dao .
COPY schemas .
COPY service .
COPY tools .
COPY views .
COPY app.py .
COPY config.py .
COPY insert_database_data.py .

RUN flask run -h 0.0.0.0 -p 80