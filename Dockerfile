# Use the selenium/standalone-firefox image as the base image
FROM selenium/standalone-firefox:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the geckodriver executable into the container
#COPY geckodriver_path/geckodriver /usr/local/bin/

# Set executable permissions for geckodriver
#RUN sudo chmod +x /usr/local/bin/geckodriver

# Install pip and other dependencies
RUN sudo apt-get update && sudo apt-get install -y python3-pip


# Copy the Python code, templates, session file, and other files into the container
COPY main.py /app/
COPY engine.py /app/
COPY datastorage.py /app/
COPY webdriver_setup.py /app/
COPY templates /app/templates
COPY static /app/static
COPY error_log.txt /app/error_log.txt
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point for the container
CMD ["python3", "main.py"]
