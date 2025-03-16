#!/bin/bash
rm -rf /opt/render/project/src/.venv
apt-get update
apt-get install -y openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> /etc/environment
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/environment
source /etc/environment
java -version
