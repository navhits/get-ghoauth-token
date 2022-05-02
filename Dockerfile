FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8000
ENTRYPOINT [ "python", "get_gho.py"]