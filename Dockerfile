# Base image
FROM python:3.7.4-stretch

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Depencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN pip install -r /requirements.txt

# Copying over files
COPY /src /src
WORKDIR /src

# Running program
CMD ["python3", "main.py"]