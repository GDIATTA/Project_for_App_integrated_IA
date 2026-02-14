FROM python:3.11
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
 && apt-get update && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

COPY . .
EXPOSE 5000

CMD ["gunicorn","-w","2","-b","0.0.0.0:5000","app:app"]