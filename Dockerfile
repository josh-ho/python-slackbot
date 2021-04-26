# syntax=docker/dockerfile:1.2
FROM python:3.9-slim
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]