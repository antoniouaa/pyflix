FROM ubuntu:20.04

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt -y update && \
    apt -y upgrade && \
    apt -y install python3 python3-pip kmod kbd

COPY . /pyflix
WORKDIR /pyflix

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--bind=0.0.0.0:80", "wsgi:create_app()"]
