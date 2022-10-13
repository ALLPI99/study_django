FROM python:3.8-slim
WORKDIR /apps
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000/tcp
