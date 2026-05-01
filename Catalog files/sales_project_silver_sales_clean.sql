-- DDL for sales_project.silver.sales_clean
-- Generated on: 2026-05-01 06:22:59.807737

CREATE TABLE sales_project.silver.sales_clean (
  order_id STRING COLLATE UTF8_BINARY,
  order_date DATE,
  sales_rep_id STRING COLLATE UTF8_BINARY,
  region STRING COLLATE UTF8_BINARY,
  city STRING COLLATE UTF8_BINARY,
  category STRING COLLATE UTF8_BINARY,
  sub_category STRING COLLATE UTF8_BINARY,
  channel STRING COLLATE UTF8_BINARY,
  quantity INT,
  unit_price DOUBLE,
  discount_pct INT,
  discount_amount DOUBLE,
  revenue DOUBLE,
  cogs DOUBLE,
  profit DOUBLE,
  year INT,
  month INT,
  quarter INT,
  Month_name STRING COLLATE UTF8_BINARY,
  day INT,
  day_name STRING COLLATE UTF8_BINARY,
  profit_margin DOUBLE,
  avg_order_value DOUBLE)
USING delta
DEFAULT COLLATION UTF8_BINARY
TBLPROPERTIES (
  'delta.enableDeletionVectors' = 'true',
  'delta.feature.appendOnly' = 'supported',
  'delta.feature.deletionVectors' = 'supported',
  'delta.feature.invariants' = 'supported',
  'delta.minReaderVersion' = '3',
  'delta.minWriterVersion' = '7',
  'delta.parquet.compression.codec' = 'zstd')

