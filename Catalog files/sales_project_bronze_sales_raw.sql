-- DDL for sales_project.bronze.sales_raw
-- Generated on: 2026-05-01 06:22:59.280090

CREATE TABLE sales_project.bronze.sales_raw (
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
  profit DOUBLE)
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

