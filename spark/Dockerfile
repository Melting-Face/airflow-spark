FROM apache/spark-py:v3.2.2

WORKDIR /opt/spark/work-dir

USER 0

COPY . .

RUN sh build.sh

WORKDIR /opt/spark

USER 185
