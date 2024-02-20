FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt .

# Install or upgrade dependencies including Flask and Werkzeug
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install --no-cache-dir Flask --upgrade \
    && pip3 install --no-cache-dir Werkzeug --upgrade

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["python3", "app.py"]
