FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installazione librerie GIS di sistema
RUN apt-get update && apt-get install -y \
    binutils libproj-dev gdal-bin libgeos-dev \
    libgdal-dev python3-dev g++ pkg-config postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Variabili per GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

# Installazione GDAL armonizzata e requisiti
RUN pip install --no-cache-dir GDAL==$(gdal-config --version)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
