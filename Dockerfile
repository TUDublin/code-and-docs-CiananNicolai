FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
WORKDIR /app 
COPY requirements.txt /app
RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

RUN apk update \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8080"]

#FROM builder as dev-envs
#RUN <<EOF
#apk update
#apk add git
#EOF
