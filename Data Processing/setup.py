# Databricks notebook source
# DBTITLE 1,Create a catalog
# MAGIC %sql
# MAGIC create catalog if not exists Sales_project;

# COMMAND ----------

# DBTITLE 1,create a Schema
# MAGIC %sql
# MAGIC create schema if not exists sales_project.bronze;
# MAGIC create schema if not exists sales_project.silver;
# MAGIC create schema if not exists sales_project.gold;

# COMMAND ----------

# DBTITLE 1,Cell 3
# MAGIC %sql
# MAGIC SHOW SCHEMAS IN sales_project;