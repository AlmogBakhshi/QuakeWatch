FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN apt update && pip install -r requirements.txt
CMD ["python","app.py"]
