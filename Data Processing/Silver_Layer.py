# Databricks notebook source
# DBTITLE 1, Read a data from Bronze  Schmea
from pyspark.sql.functions import *
from pyspark.sql.types import DataType, DoubleType, IntegerType

df_Bronze=spark.table("sales_project.bronze.sales_raw")

# COMMAND ----------

# DBTITLE 1,cast column types
df_Silver= (
    df_Bronze
    .withColumn("order_date", to_date("order_date","yyyy-MM-dd"))
    .withColumn("quantity", col("quantity").cast(IntegerType()))
    .withColumn("discount_pct", col("discount_pct").cast(IntegerType()))
    .withColumn("unit_price", col("unit_price").cast(DoubleType()))
    .withColumn("discount_amount", col("discount_amount").cast(DoubleType()))
    .withColumn("revenue", col("revenue").cast(DoubleType()))
    .withColumn("cogs", col("cogs").cast(DoubleType()))
    .withColumn("profit", col("profit").cast(DoubleType()))
)


# COMMAND ----------

# DBTITLE 1,Drop Duplicates
df_Silver= df_Silver.dropDuplicates(["order_id"])
display(df_Silver)

# COMMAND ----------

# DBTITLE 1,Check null values
from pyspark.sql.functions import col, count, when

df_Silver.select(count(when(col("order_id").isNull(), True)).alias("Order_Id_null")).show()

# COMMAND ----------

# DBTITLE 1,Filter null values
df_Silver = df_Silver.filter(col("order_id").isNotNull() & col("revenue").isNotNull())
display(df_Silver)

# COMMAND ----------

# DBTITLE 1,Derived columns
df_Silver= (
    df_Silver
    .withColumn("year", year("order_date"))
    .withColumn("month", month("order_date"))
    .withColumn("quarter",quarter("order_date"))
    .withColumn("Month_name", date_format("order_date", "MMMM"))
    .withColumn("day",dayofmonth("order_date"))
    .withColumn("day_name",date_format("order_date","E"))
)
display(df_Silver)

# COMMAND ----------

# DBTITLE 1, derived a new columns
df_Silver=(
    df_Silver
        .withColumn("profit_margin", round((col("profit") / col("revenue")) * 100, 2)) 
        .withColumn("avg_order_value",round(col("revenue") / col("quantity"), 2))
)

display(df_Silver)

# COMMAND ----------

# DBTITLE 1,standardise string columns
df_Silver=(
    df_Silver
        .withColumn("region",initcap(trim(col("region"))))
        .withColumn("city",initcap(trim(col("city"))))
        .withColumn("category",initcap(trim(col("category"))))
        .withColumn("sub_category",initcap(trim(col("sub_category"))))
        .withColumn("channel",initcap(trim(col('channel'))))
)

display(df_Silver)

# COMMAND ----------

# DBTITLE 1,write  to Silver table in Silver Schema
df_Silver.write.format('delta').mode('overwrite').option('overwriteSchema','true').saveAsTable('sales_project.silver.sales_clean')

# COMMAND ----------

# DBTITLE 1,Validation
# MAGIC %sql
# MAGIC select * from sales_project.silver.sales_clean;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     year, month_name,
# MAGIC     COUNT(*)            AS orders,
# MAGIC     ROUND(SUM(revenue), 0)  AS total_revenue,
# MAGIC     ROUND(AVG(profit_margin), 1) AS avg_margin_pct
# MAGIC FROM sales_project.silver.sales_clean
# MAGIC GROUP BY year, month_name, month
# MAGIC ORDER BY year, month;