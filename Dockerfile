FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 1024
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1024"]