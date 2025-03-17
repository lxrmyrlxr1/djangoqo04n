# 使用 Python 3.8-slim 作为基础镜像（你也可以根据需要更换版本）
FROM python:3.7.7

# 更新包列表并安装系统依赖：安装 OpenJDK 11
RUN apt-get update && apt-get install -y \
    openjdk-11-jre-headless \
    openjdk-11-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

# 设置 JAVA_HOME 环境变量，确保 pyspark 能找到 Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# 设置工作目录
WORKDIR /app

# 复制项目代码到镜像中
COPY . /app

# 升级 pip 并安装 Python 依赖
RUN pip install --upgrade pip && pip install -r requirements.txt

# 如果你需要收集静态文件，请取消下一行注释（也可以在运行时跳过）
# RUN python manage.py collectstatic --noinput

# 指定启动命令，使用 gunicorn 启动 Django 应用
CMD gunicorn dj2.wsgi:application --bind 0.0.0.0:$PORT
