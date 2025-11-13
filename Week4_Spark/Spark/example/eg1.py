import sys
import os

os.environ['JAVA_HOME'] = "C:/Program Files/Java/jdk-21.0.9"
os.environ['SPARK_HOME'] = "C:\Revature Training\Week4_Spark\Spark\.venv\Lib\site-packages\pyspark"
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Local pyspark") \
    .master("local[*]")\
    .getOrCreate()

sc = spark.sparkContext

numbers = [1,2,3,4,5]
rdd = sc.parallelize(numbers)
print("Original:",rdd.collect())

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("Name", StringType(),True),
    StructField("Age", IntegerType(),True)

])
data = [("alice",24),("bob",39)]
df = spark.createDataFrame(data, schema)

df.printSchema()
df.show()
