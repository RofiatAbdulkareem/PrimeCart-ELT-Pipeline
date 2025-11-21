import os
import boto3
from airflow.models import Variable
import pandas as pd
import awswrangler as wr

def extract_and_load_to_s3():
    access = Variable.get('ACCESS_KEY')
    secret = Variable.get('SECRET_KEY')
    region = Variable.get('REGION')
    bucket = "aws-elt-bucket"

    session = boto3.Session(
        aws_access_key_id= access,
        aws_secret_access_key= secret,
        region_name= region
    )

    datasets = {
        "products":"../data/products.csv",
        "sales":"../data/sales.csv"
    }

    for name, path in datasets.items():
        if os.path.exists(path):
            df = pd.read_csv(path, encoding= 'latin1')
            wr.s3.to_parquet(
                df=df,
                path=f"s3://{bucket}/raw/{name}",
                index=False,
                mode='overwrite',
                dataset=True,
                boto3_session=session
            )
        else:
            print(f'{path} does not exist')
    return "Data extracted and loaded to S3 successfully."    