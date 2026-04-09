<<<<<<< HEAD
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    chromium \
    chromium-driver

COPY . .

=======
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

>>>>>>> 86e35b029003c6099c3e627faebacbd8917d2905
CMD ["python", "app.py"]