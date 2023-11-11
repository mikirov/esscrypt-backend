FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Command to run the application
CMD ["gunicorn", "esscrypt.wsgi:application", "--bind", "0.0.0.0:8000"]
