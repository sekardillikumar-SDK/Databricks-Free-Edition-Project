-- DDL for sales_project.gold.rep_performance
-- Generated on: 2026-05-01 06:23:00.665437

CREATE TABLE sales_project.gold.rep_performance (
  sales_rep_id STRING COLLATE UTF8_BINARY,
  Total_orders BIGINT,
  revenue DOUBLE,
  profit DOUBLE,
  avg_margin DOUBLE,
  revenue_rank INT)
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

