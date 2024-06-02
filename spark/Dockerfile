FROM apache/spark-py:v3.2.4

WORKDIR /opt/spark/work-dir

USER 0

COPY . .

RUN sh build.sh

USER 185
