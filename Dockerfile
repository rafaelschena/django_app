FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
