FROM python:3.6

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./fastAPI_immo ./fastAPI_immo

CMD ["python", "./FASTAPI_immo/main.py"]