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


from pyspark.sql import SparkSession

# Step 1: Create Spark session
spark = SparkSession.builder \
    .appName("RDD Example") \
    .getOrCreate()

# Step 2: Get SparkContext from SparkSession
sc=spark.sparkContext

numbers=[1,2,3,4,5]
rddnum = sc.parallelize(numbers)
print("Original RDD:", rddnum.collect())
print(rddnum.first())
'''
doubled = rddnum.map(lambda x: x*2)
print('type:',type(doubled))
print("Doubled RDD:", doubled.collect())

evennum= rddnum.filter(lambda x: x%2==0)
print('type:', type(evennum))
print("Even Numbers:",evennum.collect())

total = rddnum.reduce(lambda a,b : a+b)
print('type:', type(total))
print('Sum:', total)


lines = sc.parallelize(["hello world", "hello spark","hello RDD"])
words= lines.flatMap(lambda line: line.split(" "))
print(words.collect())
word_pairs = words.map(lambda word: (word, 1))
print(word_pairs.collect())
word_counts = word_pairs.reduceByKey(lambda a, b :a+b)
print("Word Count:", word_counts.collect())


data =[("Alice",25),("Bob",30),("Charlie",28)]
df=spark.createDataFrame(data,["Name","Age"])

df.show()



high_mark1 = spark.sql("select name, mark1 from students where mark1>70")
high_mark1.show()

mark2_avg= spark.sql("select dept, avg(mark2) as avg from students group by dept order by avg")
mark2_avg.show()

data=[10,35,22,89,56,100]
rdd= sc.parallelize(data)
max_value=rdd.max()
print('Max Value:', max_value)

min_value=rdd.min()
print('Min Value:', min_value)

size = rdd.count()
print('Count:', size)
'''


data =[("a",10),("b",2),("a",5),("b",20)]
pairRDD = sc.parallelize(data)
print('Original :', pairRDD.collect())

sumByKey = pairRDD.reduceByKey(lambda x, y : x+y)
print('Reduced:',sumByKey.collect())


'''lines = sc.parallelize(["hello world","hello spark","hello RDD"])
words = lines.flatMap(lambda line: line.split(" "))
print(words.collect())
word_pairs=words.map(lambda word: (word, 1))
print(word_pairs.collect())
word_count = word_pairs.reduceByKey(lambda x, y: x + y)
print(word_count.collect())'''

rdd = sc.textFile("../data/emp.txt")
print(rdd.take(5))

rdd.saveAsTextFile("../data")
