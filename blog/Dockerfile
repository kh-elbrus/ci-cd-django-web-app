FROM python:3.8.1-slim-buster

RUN useradd wagtail

LABEL name="Blog"

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /blog

RUN chown wagtail:wagtail /blog

COPY --chown=wagtail:wagtail . .

RUN mkdir -p /vol/web/media && \ 
    mkdir -p /vol/web/static && \
    chown -R wagtail:wagtail /vol/ && \ 
    chmod -R 755 /vol/web && \ 
    chmod +x ./entrypoint.sh

USER wagtail

CMD [ "entrypoint.sh" ]
