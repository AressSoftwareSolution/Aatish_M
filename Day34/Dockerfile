# Stage 1: Build stage
FROM python:3.11 AS builder

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Stage 2: Production stage
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application code
COPY . .

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]