from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
import sys
import logging

# تنظیم لاگینگ برای دیباگ و مانیتورینگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_spark_session(app_name="WordCount"):
    """
    ایجاد یک SparkSession با تنظیمات بهینه برای اجرا در محیط محلی یا Kubernetes.

    Args:
        app_name (str): نام برنامه Spark

    Returns:
        SparkSession: نمونه SparkSession
    """
    try:
        spark = SparkSession.builder \
            .appName(app_name) \
            .config("spark.executor.memory", "1g") \
            .config("spark.driver.memory", "1g") \
            .getOrCreate()
        logger.info("SparkSession created successfully")
        return spark
    except Exception as e:
        logger.error(f"Failed to create SparkSession: {str(e)}")
        sys.exit(1)


def word_count(spark, input_path):
    """
    شمارش کلمات در یک فایل متنی با استفاده از PySpark.

    Args:
        spark (SparkSession): نمونه SparkSession
        input_path (str): مسیر فایل ورودی

    Returns:
        DataFrame: دیتافریمی با تعداد کلمات
    """
    try:
        # خواندن فایل متنی
        df = spark.read.text(input_path)
        logger.info(f"Read input file: {input_path}")

        # تبدیل متن به کلمات و شمارش
        words = df.select(explode(split(df.value, " ")).alias("word"))
        word_counts = words.groupBy("word").count()

        return word_counts
    except Exception as e:
        logger.error(f"Error processing word count: {str(e)}")
        sys.exit(1)


def main():
    """
    تابع اصلی برای اجرای برنامه.
    """
    # بررسی آرگومان‌های ورودی
    if len(sys.argv) != 2:
        logger.error("Usage: spark-submit wordcount.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]

    # ایجاد SparkSession
    spark = create_spark_session()

    # اجرای شمارش کلمات
    word_counts = word_count(spark, input_path)

    # نمایش نتیجه
    word_counts.show()
    logger.info("Word count completed successfully")

    # بستن SparkSession
    spark.stop()
    logger.info("SparkSession stopped")


if __name__ == "__main__":
    main()