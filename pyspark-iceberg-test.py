import os
import findspark
from pyspark.sql import *
from pyspark import SparkConf

findspark.init()

conf = SparkConf()

conf.set("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.3,org.projectnessie.nessie-integrations:nessie-spark-extensions-3.5_2.12:0.76.3,software.amazon.awssdk:bundle:2.17.178,software.amazon.awssdk:url-connection-client:2.17.178")
conf.set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,org.projectnessie.spark.extensions.NessieSparkSessionExtensions")

conf.set("spark.sql.execution.pyarrow.enabled", "true")

AWS_REGION = "us-east-1"
AWS_DEFAULT_REGION = "us-east-1"
NESSIE_URI = "http://localhost:19120/api/v1"
MINIO_S3_ENDPOINT = "http://localhost:9000"
NESSIE_WAREHOUSE_LOCATION = "s3a://warehouse/"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_ACCESS_KEY = "minioadmin"

conf.set('spark.sql.catalog.nessie', 'org.apache.iceberg.spark.SparkCatalog')
conf.set('spark.sql.catalog.nessie.uri', NESSIE_URI)
conf.set('spark.sql.catalog.nessie.ref', 'main')
conf.set('spark.sql.catalog.nessie.authentication.type', 'NONE')
conf.set('spark.sql.catalog.nessie.catalog-impl', 'org.apache.iceberg.nessie.NessieCatalog')
conf.set('spark.sql.catalog.nessie.s3.endpoint', MINIO_S3_ENDPOINT)
conf.set('spark.sql.catalog.nessie.warehouse', NESSIE_WAREHOUSE_LOCATION)
conf.set('spark.sql.catalog.nessie.io-impl', 'org.apache.iceberg.aws.s3.S3FileIO')
conf.set('spark.hadoop.fs.s3a.access.key', MINIO_ACCESS_KEY)
conf.set('spark.hadoop.fs.s3a.secret.key', MINIO_SECRET_ACCESS_KEY)

spark = SparkSession.builder.config(conf=conf).remote("sc://localhost:15002").getOrCreate()
print("Spark running")

spark.sql("DROP TABLE IF EXISTS nessie.subjects"),
spark.sql("CREATE TABLE nessie.subjects (subject STRING) USING iceberg").show()
spark.sql("INSERT INTO nessie.subjects VALUES ('Math'), ('Social Studies'), ('Geography')").show()
spark.sql("SELECT * FROM nessie.subjects").show()
print("SQL execution done")

# spark.sql("CREATE BRANCH work IN arctic").toPandas()
# spark.sql("USE REFERENCE work IN arctic")

# spark.sql(
#     """CREATE TABLE IF NOT EXISTS arctic.salesdip.sales
#             (id STRING, name STRING, product STRING, price STRING, date STRING) USING iceberg"""
# )

# spark.sql(
#     """CREATE OR REPLACE TEMPORARY VIEW salesview USING csv
#             OPTIONS (path "salesdata.csv", header true)"""
# )
# spark.sql("INSERT INTO arctic.salesdip.sales SELECT * FROM salesview")

# spark.sql("SELECT * FROM arctic.salesdip.sales LIMIT 5").toPandas()
