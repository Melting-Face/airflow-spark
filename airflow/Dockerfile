FROM apache/airflow:2.9.3-python3.10

WORKDIR /opt/airflow

COPY . .

USER 0

RUN sh ./setup.sh

ENV JAVA_HOME=/usr/lib/jvm/msopenjdk-11-arm64

USER airflow

RUN pip install --no-cache-dir -r requirements.txt
