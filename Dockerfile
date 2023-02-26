FROM python:3.8.16-slim

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "scripts/update_release.py"]
