FROM apache/airflow:2.9.3-python3.10

WORKDIR /opt/airflow

COPY . .

USER 0

RUN apt-get update -y && \
    apt install openjdk-17-jre-headless -y

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64

USER airflow

RUN pip install --no-cache-dir -r requirements.txt
