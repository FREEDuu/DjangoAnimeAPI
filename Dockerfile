# Set the base image
ARG PYTHON_VERSION=3.10-slim-bullseye
FROM python:${PYTHON_VERSION}

# Set environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create the /code directory inside the container
RUN mkdir -p /code

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file to the container
COPY requirements.txt /tmp/requirements.txt

# Install the dependencies
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy the rest of the application into the container
COPY . /code

# Expose port 8071 (this is just a "documentation" and is not a binding)
EXPOSE 8071

# Run the application with gunicorn
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8071 --workers 2 animeApi.wsgi"]
