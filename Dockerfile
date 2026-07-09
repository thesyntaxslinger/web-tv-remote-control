FROM python:3.14-alpine AS builder

WORKDIR /build

RUN apk add --no-cache \
    linux-headers \
    build-base

COPY . .

RUN pip wheel --no-cache-dir --wheel-dir=/wheels .



FROM python:3.14-alpine

WORKDIR /app

COPY --from=builder /wheels /wheels

RUN pip install --no-cache-dir /wheels/*

RUN rm -rf /wheels

EXPOSE 8080

CMD ["web-tv-remote-control"]
