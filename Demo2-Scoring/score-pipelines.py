from pysparkling import *
from pysparkling.ml import *
import sys
from pyspark.sql.types import *
import time
from pyspark.sql import *
from pysparkling.initializer import Initializer
from pyspark.ml import Pipeline, PipelineModel

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("OFF")

# Add sparkling water to all spark executors
Initializer.load_sparkling_jar(spark)

print(sys.argv[1])
mojo1 = PipelineModel.load(sys.argv[2])
print("Spark Pipeline Loaded")

print(sys.argv[1])
mojo2 = H2OMOJOPipelineModel.create_from_mojo(sys.argv[1])
print("Driverless AI as Spark Pipeline Loaded")


schema = StructType([
    StructField("GPU", BooleanType(), True),
    StructField("sys_CPU", DoubleType(), True),
    StructField("sys_GPU", DoubleType(), True),
    StructField("config_accu", DoubleType(), True),
    StructField("config_time", DoubleType(), True),
    StructField("config_MLI", DoubleType(), True),
    StructField("nrows_train", DoubleType(), True),
    StructField("ncols_train", DoubleType(), True),
    StructField("target_binary_dist", DoubleType(), True),
    StructField("target_nclasses", DoubleType(), True),
    StructField("recipe_individuals", DoubleType(), True),
    StructField("train_data_size", DoubleType(), True),
    StructField("weight", IntegerType(), True)])

input_data_stream = spark.readStream.schema(schema).csv("s3a://h2o-spark-summit-data/*.csv")
output_data_stream_1 = mojo1.transform(input_data_stream)
output_data_stream_2 = mojo2.transform(input_data_stream)

output_data_stream_1.writeStream.format("memory").queryName("spark").start()
output_data_stream_2.writeStream.format("memory").queryName("dai").start()

while True:
   time.sleep(2)
   print("Showing Results from Spark")
   spark.sql("select * FROM spark").show()
   print("Showing Results from DAI")
   spark.sql("select * FROM dai").show()

