# استفاده از تصویر پایه رسمی Apache Spark
FROM apache/spark:3.5.0

# تنظیم کاربر root برای نصب بسته‌ها
USER root

# نصب Python و pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pyspark==3.5.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache/pip

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل برنامه PySpark و فایل ورودی
COPY wordcount.py /app/wordcount.py
COPY input.txt /app/input.txt

# دستور اجرای برنامه با spark-submit
CMD ["/opt/spark/bin/spark-submit", "/app/wordcount.py", "/app/input.txt"]