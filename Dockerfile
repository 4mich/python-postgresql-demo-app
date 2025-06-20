FROM python:3.13.5-slim-bullseye
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR src
EXPOSE 8080
ENTRYPOINT ["python", "main.py"]