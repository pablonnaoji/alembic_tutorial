# pull official base image
FROM python:3.9.4-alpine

# set work directory
WORKDIR /usr/project/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/project/app/requirements.txt

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/project/app/requirements.txt

COPY . /usr/project/app/

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]