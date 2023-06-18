# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the port your Flask application is running on
EXPOSE 8080

# Set the command to run your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

# Build and run the Docker image:
# docker build -t flask-api-image .
# docker run -p 5000:5000 flask-api-image
