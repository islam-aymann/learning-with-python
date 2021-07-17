FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get --no-install-recommends -y install python3.7-dev build-essential && \
    apt-get install -y curl jq git nano && \
    # Pillow dependencies
    apt-get install -y python-pil && \
    # CFFI dependencies
    apt-get install -y libffi-dev python-cffi

RUN yes | apt-get install redis-server apache2-utils


# install dependencies
RUN python -m pip install -U pip
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

WORKDIR /opt/project/demo
COPY . /opt/project/demo

CMD python manage.py migrate