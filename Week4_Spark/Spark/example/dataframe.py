import  sys
import os

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType



os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21.0.9"
os.environ["SPARK_HOME"] = "C:\Revature Training\Week4_Spark\Spark\.venv\Lib\site-packages\pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName('Local Pyspark')\
    .getOrCreate()

sc = spark.sparkContext

from pyspark.sql.types import StringType,StructField,IntegerType,StructType

myschema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("_corrupt_record", StringType(), True)
])

df = spark.read.json(path="../data/file1.json", schema=myschema)
df.show()
df.printSchema()

df.createOrReplaceTempView("people")
spark.sql("SELECT name FROM people WHERE age > 28").show()

df.write.json("../data/output.json")



data =[("Alice",25),("Bob",30),("Charlie",35)]
columns = ["name","age"]

df= spark.createDataFrame(data,columns)
df.show()

df.write.mode("overwrite").parquet("../data/file2.parquet")
df = spark.read.parquet("../data/file2.parquet")
df.show()

