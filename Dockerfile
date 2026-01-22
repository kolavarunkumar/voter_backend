# Base image
FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files (if possible)
RUN python manage.py collectstatic --noinput || echo "Skipping static collection"

# Expose port
EXPOSE 8000

# Run migrations & start server
CMD bash -c "python manage.py migrate && gunicorn your_project.wsgi:application --bind 0.0.0.0:8000"
