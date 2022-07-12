FROM arm64v8/python:3

RUN useradd stt

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

EXPOSE 8080

RUN mkdir /usr/bin/sharethetrail-site

WORKDIR /usr/bin/sharethetrail-site/

COPY ./requirements.txt /usr/bin/sharethetrail-site/
COPY ./manage.py /usr/bin/sharethetrail-site/
COPY ./docker-compose.yml /usr/bin/sharethetrail-site/
COPY ./sharethetrail/ /usr/bin/sharethetrail-site/sharethetrail/

RUN pip install "gunicorn==20.0.4"
RUN pip install -r /usr/bin/sharethetrail-site/requirements.txt

RUN chown -R stt:stt /usr/bin/sharethetrail-site

USER stt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]
