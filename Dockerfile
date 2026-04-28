# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
# Add any other necessary packages here
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Define the command to run the application using Uvicorn (FastAPI server)
# This assumes your FastAPI app instance is named 'app' and lives in 'main.py'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
