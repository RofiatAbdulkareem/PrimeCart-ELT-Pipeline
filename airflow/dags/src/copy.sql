TRUNCATE TABLE analytics.sales_summarys;

COPY analytics.sales_summarys
FROM 's3://aws-elt-bucket/gold/sales_summary/'
IAM_ROLE 'arn:aws:iam::819340487562:role/RedshiftServerlessRole'
FORMAT AS PARQUET;