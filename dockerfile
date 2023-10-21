# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE "jwt_implementation.settings" 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
