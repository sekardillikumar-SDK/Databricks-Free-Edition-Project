Sfrom pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(
    comment="Bronze layer: Raw sales data ingested from sales_project.bronze.sales_raw"
)
def bronze_sales_raw():
    """
    Ingest raw sales data as a streaming table.
    Source: sales_project.bronze.sales_raw
    """
    return spark.readStream.option("skipChangeCommits", "true").table("sales_project.bronze.sales_raw")
