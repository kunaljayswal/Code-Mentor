# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which your application will run (if necessary)
EXPOSE 80

# Run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]
