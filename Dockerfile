
# frontent/Dockerfile

# Specify the base image
FROM python:3.9

# Copy the requirements.txt file to the app directory
COPY requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project files to the /app directory
# Include app directory to avoid copying files in the working directory itself
COPY . /app

# Expose port 8000 for the application
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
