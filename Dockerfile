FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8080
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8080"]

FROM builder as dev-envs
RUN <<EOF
apk update
apk add git
EOF
