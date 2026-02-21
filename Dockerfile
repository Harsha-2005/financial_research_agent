# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

ENV OLLAMA_BASE_URL=http://host.docker.internal:11434

# Expose nothing (CLI-based app)
CMD ["python", "main.py"]