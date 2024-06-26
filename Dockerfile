# Use a base image with Python 3.12
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code, templates, session file, and other files into the container
COPY main.py /app/
COPY engine.py /app/
COPY datastorage.py /app/
COPY webdriver_setup.py /app/
COPY templates /app/templates
COPY static /app/static
COPY error_log.txt /app/error_log.txt
COPY vcards /app/vcards
COPY cloudbuild.yaml /app/cloudbuild.yaml
COPY requirements.txt /app/requirements.txt

# Set environment variable to prevent debconf from prompting
ENV DEBIAN_FRONTEND=noninteractive

# Install apt-utils to avoid debconf warning
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    apt-utils \
    wget \
    bzip2 \
 && rm -rf /var/lib/apt/lists/*



 RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
        wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-115.0esr-SSL&os=linux64&lang=en-US" && \
        tar xjf $FIREFOX_SETUP -C /opt/ && \
        ln -s /opt/firefox/firefox /usr/bin/firefox && \
        rm $FIREFOX_SETUP

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download and install geckodriver
ARG GECKODRIVER_VERSION=0.34.0
RUN apt-get update \
     && apt-get install -y wget unzip \
     && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
     && tar -xvzf geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
     && mv geckodriver /usr/local/bin/ \
     && chmod +x /usr/local/bin/geckodriver \
     && rm geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

# Expose port 80
EXPOSE 8080

# Set the entry point for the container
CMD ["python3", "main.py"]
