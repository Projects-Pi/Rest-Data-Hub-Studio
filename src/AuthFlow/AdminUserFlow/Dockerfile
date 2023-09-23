FROM python:3.6-slim-buster

# Create and set the working directory
WORKDIR /api/v1/app

# Copy the entire project directory into the container
COPY /api /api

# Install the required Python packages
RUN pip install -r /api/v1/app/requirements.txt

# Expose the port your Flask application will run on
EXPOSE 4001

# Define the command to start your Flask application
CMD ["python3", "app.py"]
