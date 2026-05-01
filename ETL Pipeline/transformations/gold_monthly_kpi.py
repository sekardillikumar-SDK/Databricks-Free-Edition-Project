from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(
    comment="Gold layer: Monthly KPI aggregations for time-based analysis",
    cluster_by=["year", "month"]
)
def gold_monthly_kpi():
    """
    Monthly sales KPIs and trends.
    Business KPI: Time-based performance tracking.
    """
    return (
        spark.read.table("silver_sales_cleaned_mv")
        .groupBy("year", "month", "Month_name")
        .agg(
            F.countDistinct("order_id").alias("total_orders"),
            F.round(F.sum("revenue"), 0).alias("total_revenue"),
            F.round(F.sum("profit"), 0).alias("total_profit"),
            F.round(F.sum("quantity"), 0).alias("unit_sold"),
            F.round(F.avg("profit_margin"), 2).alias("avg_profit_margin"),
            F.countDistinct("sales_rep_id").alias("active_reps"),
            F.countDistinct("category").alias("categories_sold"),
            F.round(F.sum("discount_amount"), 0).alias("total_discounts")
        )
        .orderBy("year", "month")
    )
