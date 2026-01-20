FROM python:3.11-slim
# Install database drivers
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install flask psycopg2-binary
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]