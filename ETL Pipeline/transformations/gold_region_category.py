from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(
    comment="Gold layer: Sales performance by region, category, and channel",
    cluster_by=["region", "category"]
)
def gold_region_category():
    """
    Aggregate sales metrics by region, category, and channel.
    Business KPI: Regional performance analysis.
    """
    return (
        spark.read.table("silver_sales_cleaned_mv")
        .groupBy("region", "category", "channel")
        .agg(
            F.count("order_id").alias("orders"),
            F.round(F.sum("revenue"), 0).alias("revenue"),
            F.round(F.sum("profit"), 0).alias("profit"),
            F.round(F.avg("profit_margin"), 2).alias("avg_margin"),
            F.round(F.sum("discount_amount"), 0).alias("total_discount"),
            F.round(F.sum("quantity"), 0).alias("units_sold"),
            F.countDistinct("sales_rep_id").alias("active_reps")
        )
        .orderBy(F.desc("revenue"))
    )
