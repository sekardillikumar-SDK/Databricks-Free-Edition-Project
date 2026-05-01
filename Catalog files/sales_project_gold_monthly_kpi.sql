-- DDL for sales_project.gold.monthly_kpi
-- Generated on: 2026-05-01 06:23:00.086017

CREATE TABLE sales_project.gold.monthly_kpi (
  year INT,
  month INT,
  month_name STRING COLLATE UTF8_BINARY,
  total_orders BIGINT,
  total_revenue DOUBLE,
  total_profit DOUBLE,
  unit_sold BIGINT,
  avg_profit_margin DOUBLE,
  active_reps BIGINT)
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

