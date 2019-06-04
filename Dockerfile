FROM python:3.7


WORKDIR /
RUN apt-get update
RUN apt-get install xvfb libfontconfig  wget libssl1.0-dev -y
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
ENV WKHTMLTOPDF_PATH=/wkhtmltox/bin/wkhtmltopdf

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
CMD exec gunicorn convertor.wsgi --bind 0.0.0.0:8000 --workers 3
