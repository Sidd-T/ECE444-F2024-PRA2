FROM python:3.11-slim

WORKDIR /ECE444-F2024-PRA2

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=hello.py

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]