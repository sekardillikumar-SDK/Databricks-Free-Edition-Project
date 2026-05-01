from pyspark import pipelines as dp
from pyspark.sql import functions as F
from pyspark.sql.window import Window

@dp.materialized_view(
    comment="Gold layer: Sales representative performance metrics and rankings",
    cluster_by=["sales_rep_id"]
)
def gold_rep_performance():
    """
    Calculate sales rep performance with revenue rankings.
    Business KPI: Rep productivity and effectiveness.
    """
    return (
        spark.read.table("silver_sales_cleaned_mv")
        .groupBy("sales_rep_id")
        .agg(
            F.count("order_id").alias("Total_orders"),
            F.round(F.sum("revenue"), 0).alias("revenue"),
            F.round(F.sum("profit"), 0).alias("profit"),
            F.round(F.avg("profit_margin"), 2).alias("avg_margin"),
            F.round(F.sum("quantity"), 0).alias("units_sold")
        )
        .withColumn(
            "revenue_rank",
            F.dense_rank().over(Window.orderBy(F.desc("revenue")))
        )
        .orderBy(F.desc("revenue"))
    )
