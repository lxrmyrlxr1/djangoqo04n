# Use Python 3.8-slim as the base mirror (you can also change the version as needed)
FROM python:3.7.7
# Update the package list and install the system dependency: Install the OpenJDK 11
RUN apt-get update && apt-get install -y \
openjdk-11-jre-headless \
openjdk-11-jdk-headless \
&& rm -rf /var/lib/apt/lists/*
# Set the JAVA _ HOME environment variable to ensure that the pyspark can find the Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"
# Set up the working directory
WORKDIR /app
# Copy the item code into the mirror
COPY . /app
# Upgrade the pip, and install the Python dependency
RUN pip install --upgrade pip && pip install -r requirements.txt
# If you need to collect static files, cancel the next comment (you can skip at runtime)
# RUN python manage.py collectstatic --noinput
# Specify the start command to start the Django application using the gunicorn
CMD gunicorn dj2.wsgi:application --bind 0.0.0.0:$PORT
