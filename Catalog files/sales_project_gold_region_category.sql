-- DDL for sales_project.gold.region_category
-- Generated on: 2026-05-01 06:23:00.402251

CREATE TABLE sales_project.gold.region_category (
  region STRING COLLATE UTF8_BINARY,
  category STRING COLLATE UTF8_BINARY,
  channel STRING COLLATE UTF8_BINARY,
  orders BIGINT,
  revenue DOUBLE,
  profit DOUBLE,
  avg_margin DOUBLE,
  total_discount DOUBLE)
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

