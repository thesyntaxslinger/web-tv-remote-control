FROM python:3.14-alpine AS builder

WORKDIR /build

RUN apk add --no-cache \
    linux-headers \
    build-base
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip wheel --no-cache-dir --wheel-dir=/wheels .




FROM python:3.14-alpine

WORKDIR /app

RUN apk add --no-cache su-exec
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    gosu \
#    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*
RUN rm -rf /wheels

ENV PORT=8080
ENV HOST=0.0.0.0
ENV PUID=1000
ENV PGID=1000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["web-tv-remote-control"]
