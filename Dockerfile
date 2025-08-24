# Use Python 3.11-slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory (which contains main.py) into the container
COPY ./app ./app

# Copy the model directory (containing the trained model)
COPY ./model /model

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
