from pysparkling import *
from pysparkling.ml import *
from pysparkling.initializer import Initializer
from pyspark.ml import Pipeline, PipelineModel
import sys
from pyspark.sql.types import *
import time

from pyspark.sql import *
spark = SparkSession.builder.getOrCreate()
# Add sparkling water to all spark executors
Initializer.load_sparkling_jar(spark)

print(sys.argv[1])
mojo = PipelineModel.load(sys.argv[1])
print("Mojo Pipeline Loaded")

spark.sparkContext.setLogLevel("OFF")
schema = StructType([
    StructField("ID", StringType(), True),
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
output_data_stream = mojo.transform(input_data_stream)
output_data_stream.writeStream.format("memory").queryName("predictions").start()

def readable_time(sec_as_double):
  sec=int(sec_as_double)
  if sec < 60:
    return str(sec) + " s"
  elif sec < 60*60:
    return str(sec/60) + " min " + str(sec-(sec/60)*60) + " s"
  elif sec < 60*60*60:
    hours=sec/3600
    mins=(sec-hours*3600)/60
    s=(sec - hours*3600 - mins*60)
    return str(hours) + " hours " + str(mins) + " min " + str(s) + " s"
  else:
    return "long time"   


spark.udf.register("readable_time", readable_time)


while True:
   time.sleep(2)
   print("Showing Results")
   spark.sql("select unix_timestamp(current_timestamp()) as Timestamp, readable_time(prediction_output.value) as Predicted_Time from predictions").show(10, False)
