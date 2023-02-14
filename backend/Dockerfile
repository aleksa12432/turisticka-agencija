# Use an official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables 
ENV PYTHONUNBUFFERED 1

RUN python manage.py test --settings=tripify.settings_test

# Run the Django migrations
RUN python manage.py migrate

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]