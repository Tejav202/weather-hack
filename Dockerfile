# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py .

# Expose port 8080 (IBM Cloud Code Engine default)
EXPOSE 8080

# Set environment variables
ENV PORT=8080
ENV HOST=0.0.0.0

# Run the server using uvicorn
CMD ["uvicorn", "server:mcp.app", "--host", "0.0.0.0", "--port", "8080"]