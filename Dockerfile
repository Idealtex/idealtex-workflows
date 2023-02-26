FROM python:3.8.16-slim

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/scripts/update_release.py"]
