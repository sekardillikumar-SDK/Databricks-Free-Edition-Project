# Databricks notebook source
# DBTITLE 1,Read a CSV
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark=SparkSession.builder.getOrCreate()

# Read  raw CSV file
df_Raw= spark.read.csv("/Volumes/sales_project/default/stagings/sales_data.csv", header=True, inferSchema=True)

# COMMAND ----------

display(df_Raw)

# COMMAND ----------

df_Raw.printSchema()

# COMMAND ----------

# DBTITLE 1,Write  a Delta Table
df_Raw.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable("sales_project.bronze.Sales_Raw")

# COMMAND ----------

# DBTITLE 1,verfy bronze layer
# MAGIC %sql
# MAGIC select * from sales_project.bronze.Sales_Raw;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count('Order_id') as Total_order from sales_project.bronze.Sales_Raw;

# COMMAND ----------

# DBTITLE 1,check for nulls
# MAGIC %sql
# MAGIC select 
# MAGIC   count(*) - count(order_id) as Total_null_order, 
# MAGIC   count(*) - count(revenue) as Total_null_revenu,
# MAGIC   count(*) - count(order_date) as Total_null_date
# MAGIC
# MAGIC from 
# MAGIC   sales_project.bronze.Sales_Raw
# MAGIC