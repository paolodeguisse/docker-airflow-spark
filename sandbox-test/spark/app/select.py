from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession \
    .builder \
    .appName('my_darling') \
    .config('spark.driver.extraClassPath', 'postgresql-42.2.5.jar') \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://151.248.122.146:5432/airflow") \
    .option("dbtable", "active_clients") \
    .option("user", "airflow") \
    .option("password", "airflow2") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.show()
