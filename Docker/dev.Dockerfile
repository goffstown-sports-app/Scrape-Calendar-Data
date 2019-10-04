FROM python:3.6-stretch

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


COPY ./../dev-requirements.txt dev-requirements.txt
RUN pip install -r dev-requirements.txt

COPY ./../src /src

WORKDIR /src/tests
CMD ["pytest", "--emoji"]
