FROM python:3.7

RUN apt-get update
RUN apt-get install -qy python-pip
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
ADD requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /code
# Install dependencies

# Copy project
COPY . /code/