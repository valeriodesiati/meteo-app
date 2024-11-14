FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /usr/local/app

# Install the application dependencies
RUN pip install --no-cache-dir Flask python-dotenv requests

# Copy in the source code and the startup script
COPY . .

# Expose the necessary ports
EXPOSE 5000

# Run the script to start both clients
CMD ["python", "meteo.py"]
