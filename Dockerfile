# Base image
FROM python:3.6-stretch

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
COPY /scrapeCalendarData /scrapeCalendarData
RUN find . -name \*.json -type f -delete
WORKDIR /scrapeCalendarData

# Running program
CMD ["python3", "main.py"]
