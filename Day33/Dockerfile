# File: Dockerfile

# 1. Use official Python image as base
FROM python:3.11

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependencies file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code into container
COPY . .

# 5. Expose port 5000
EXPOSE 5000

# 6. Command to run app
CMD ["python", "app.py"]



# Explanation:

    # FROM → Base image

    # WORKDIR → Folder inside container

    # COPY + RUN → Copy and install dependencies

    # COPY . . → Copy all project files

    # EXPOSE → Makes port 5000 accessible

    # CMD → Runs Flask app when container starts