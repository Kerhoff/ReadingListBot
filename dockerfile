# Use the official image as a parent image
FORM python:3.12-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    POETRY_VERSION=1.6.1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

# Update PATH so the poetry bin is available
ENV PATH="${PATH}:/root/.local/bin"

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock ./

# Install the dependencies
RUN poetry install --no-root --no-dev

# Expose any necessary ports
# EXPOSE 8000

# Set the command to run the application
CMD ["python", "bot/app.py"]
