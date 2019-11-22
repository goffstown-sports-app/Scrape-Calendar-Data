# Base image
FROM jfloff/alpine-python:3.6

# Meta for Docker Hub
LABEL author matthewgleich@gmail.com

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
RUN pip3 install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# Copying over files
COPY /src /src
RUN find . -name \*.json -type f -delete
WORKDIR /src

# Running program
CMD ["python3", "main.py"]
