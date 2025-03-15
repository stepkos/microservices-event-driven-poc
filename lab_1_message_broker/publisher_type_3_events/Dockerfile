FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "-m", "application.main"]
