# Databricks notebook source
# DBTITLE 1,read data from silver Schema
# MAGIC %sql
# MAGIC select * from sales_project.silver.sales_clean;

# COMMAND ----------

# DBTITLE 1,monthly revenue KPI table
# MAGIC %sql
# MAGIC create or replace table sales_project.gold.monthly_Kpi 
# MAGIC as
# MAGIC select
# MAGIC   year, month, month_name,
# MAGIC   count(distinct order_id) as total_orders,
# MAGIC   round(sum(revenue),0) as total_revenue,
# MAGIC   round(sum(profit),0) as total_profit,
# MAGIC   round(sum(quantity),0) as unit_sold,
# MAGIC   round(avg(profit_margin),0) as avg_profit_margin,
# MAGIC   count(distinct sales_rep_id) as active_reps
# MAGIC from sales_project.silver.sales_clean
# MAGIC group by year, month, month_name
# MAGIC order by year, month;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_project.gold.monthly_Kpi;

# COMMAND ----------

# DBTITLE 1,Region & Category performance
# MAGIC %sql
# MAGIC create or replace table sales_project.gold.region_category
# MAGIC as
# MAGIC select
# MAGIC   region,  category, channel,
# MAGIC   count(distinct order_id) as orders,
# MAGIC   round(sum(revenue),0) as revenue, 
# MAGIC   round(sum(profit),0) as profit,
# MAGIC   round(sum(profit_margin),2) as avg_margin,
# MAGIC   round(sum(discount_amount),0) as total_discount
# MAGIC from sales_project.silver.sales_clean
# MAGIC group by region, category, channel
# MAGIC order by revenue desc;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_project.gold.region_category;

# COMMAND ----------

# DBTITLE 1,top sales reps
# MAGIC %sql
# MAGIC create or replace table sales_project.gold.rep_performance
# MAGIC as
# MAGIC select
# MAGIC   sales_rep_id, 
# MAGIC   count(distinct order_id) as Total_orders,
# MAGIC   round(sum(revenue),0) as revenue, 
# MAGIC   round(sum(profit),0) as profit,
# MAGIC   round(avg(profit_margin),2) as avg_margin,
# MAGIC  dense_rank() over(order by sum(revenue) desc) as revenue_rank
# MAGIC from sales_project.silver.sales_clean
# MAGIC group by sales_rep_id
# MAGIC order by revenue desc;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_project.gold.rep_performance