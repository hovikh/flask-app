# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Start Gunicorn server
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:app"]
