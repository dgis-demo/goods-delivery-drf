FROM python:3.10-slim

COPY requirements.txt /opt/app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    openssl \
    libpq-dev \
	nginx \
    binutils \
    libproj-dev \
    gdal-bin \
    python3-gdal \
    g++ \
    make
RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

COPY . /opt/app
VOLUME ["/opt/app/media"]
WORKDIR /opt/app