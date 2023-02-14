# Python image za docker
FROM python:3.8-slim-buster

# Direktorijum u kom radimo
WORKDIR /app

# Kopiranje zahteva i zavisnosti 
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiranje project fajla
COPY . .

# Okruzenje 
ENV PYTHONUNBUFFERED 1

#Izvrsava testove za Django aplikaciju
RUN python manage.py test --settings=tripify.settings_test

# Run the Django migrations
RUN python manage.py migrate

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
