FROM vaporio/python:3.6 as builder
COPY requirements.txt .

WORKDIR /build

RUN pip install --prefix=/build -r /requirements.txt --no-warn-script-location \
 && rm -rf /root/.cache

FROM vaporio/python:3.6-slim
COPY --from=builder /build /usr/local

COPY . /code
WORKDIR /code

RUN apt-get update \
 && python setup.py install

ARG VCS_REF
ARG BUILD_VERSION

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="vaporio/etamay" \
      org.label-schema.vcs-url="https://github.com/vapor-ware/etamay" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor="Vapor IO" \
      org.label-schema.version=$BUILD_VERSION \
      maintainer="marco@vapor.io"

CMD ["python", "etamay"]
