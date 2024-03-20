FROM python:slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Install make
RUN apt-get update && apt-get install -y make

CMD ["make", "run"]