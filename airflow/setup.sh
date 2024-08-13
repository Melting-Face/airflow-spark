#!/bin/sh

apt-get upgrade && apt-get update -y

apt-get install wget -y

apt install msopenjdk-11/bookworm -y

mkdir jars

while read -r line
do
  wget "https://repo1.maven.org/maven2/$line" -P /opt/airflow/jars
done < dependencies.txt
