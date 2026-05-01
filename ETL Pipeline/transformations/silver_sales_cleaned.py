from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(
    name="silver_sales_cleaned_mv",
    comment="Silver layer: Cleaned and enriched sales data with calculated metrics (Materialized View)",
    cluster_by=["region", "category"]
)
@dp.expect_or_drop("valid_order_id", "order_id IS NOT NULL")
@dp.expect_or_drop("valid_sales_rep", "sales_rep_id IS NOT NULL")
@dp.expect_or_drop("positive_quantity", "quantity > 0")
@dp.expect_or_drop("positive_revenue", "revenue >= 0")
@dp.expect("valid_discount", "discount_pct >= 0 AND discount_pct <= 100")
@dp.expect("positive_profit", "profit >= -revenue")
def silver_sales_cleaned_mv():
    """
    Clean, validate, and enrich sales data from bronze layer.
    Adds calculated fields: year, month, quarter, day, profit_margin, avg_order_value
    """
    return (
        spark.read.table("bronze_sales_raw")
        .select(
            # Original fields with trimming
            F.trim(F.col("order_id")).alias("order_id"),
            F.col("order_date"),
            F.trim(F.col("sales_rep_id")).alias("sales_rep_id"),
            F.trim(F.col("region")).alias("region"),
            F.trim(F.col("city")).alias("city"),
            F.trim(F.col("category")).alias("category"),
            F.trim(F.col("sub_category")).alias("sub_category"),
            F.trim(F.col("channel")).alias("channel"),
            F.col("quantity"),
            F.col("unit_price"),
            F.col("discount_pct"),
            F.col("discount_amount"),
            F.col("revenue"),
            F.col("cogs"),
            F.col("profit"),
            
            # Date components
            F.year("order_date").alias("year"),
            F.month("order_date").alias("month"),
            F.quarter("order_date").alias("quarter"),
            F.date_format("order_date", "MMMM").alias("Month_name"),
            F.dayofmonth("order_date").alias("day"),
            F.date_format("order_date", "E").alias("day_name"),
            
            # Calculated metrics
            F.round(
                F.when(F.col("revenue") > 0, (F.col("profit") / F.col("revenue")) * 100)
                .otherwise(0), 
                2
            ).alias("profit_margin"),
            
            F.round(
                F.when(F.col("quantity") > 0, F.col("revenue") / F.col("quantity"))
                .otherwise(F.col("revenue")), 
                2
            ).alias("avg_order_value")
        )
    )
