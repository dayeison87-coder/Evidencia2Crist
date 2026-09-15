FROM python:3.11-slim

RUN apt-get update && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app/app.py"]