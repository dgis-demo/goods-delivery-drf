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
WORKDIR /opt/app

RUN rm -v /etc/nginx/nginx.conf
ADD Deploy/nginx.conf /etc/nginx/

RUN chmod +x ./Deploy/entrypoint.sh
ENTRYPOINT ["bash", "./Deploy/entrypoint.sh"]