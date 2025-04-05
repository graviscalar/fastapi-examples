FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]