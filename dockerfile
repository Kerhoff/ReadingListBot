# Use the official image as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app
COPY . /app

# Install Poeetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

# Set the command to run the application
CMD ["python", "-m", "bot"]
