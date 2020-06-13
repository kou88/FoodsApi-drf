# ベースos
FROM ubuntu:20.04

ARG TEMPDIR=/tempdir
ENV PYTHONUNBUFFERED 1  
# 初期実行コマンド
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y vim \
    && apt-get install -y wget \
    && apt-get install -y gcc \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-distutils \
    && apt-get install -y libpq-dev \
    && apt-get install -y python3-dev \
    && wget https://bootstrap.pypa.io/get-pip.py -P ${TEMPDIR}
RUN python3 ${TEMPDIR}/get-pip.py
RUN pip install --upgrade pip
COPY ./requierments.txt ${TEMPDIR}
RUN pip install -r ${TEMPDIR}/requierments.txt
VOLUME /home/app
EXPOSE 8001
COPY app/Foods /home/app
WORKDIR /home/app
CMD gunicorn Foods.wsgi 0.0.0.0:$PORT
