# Start with a minimal Python image
FROM python:3.11-slim

# Install necessary system dependencies for Vyper
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Vyper and Python packages
RUN pip install --no-cache-dir vyper aiohttp aiofiles

# Copy the server script into the container
COPY server.py /server.py

# Set the working directory
WORKDIR /code

# Expose the desired port
EXPOSE 8000

# Run the aiohttp server
CMD ["python3", "/server.py"]
