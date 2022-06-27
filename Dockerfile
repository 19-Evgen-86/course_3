FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY dao .
COPY schemas .
COPY service .
COPY tools .
COPY views .
COPY app.py .
COPY config.py .
COPY insert_database_data.py .

RUN python - m flask run -h 0.0.0.0 -p 80