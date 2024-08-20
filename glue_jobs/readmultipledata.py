import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


csv_path = "s3://bucket-de-entrada/csv/"
csv_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    format_options={"withHeader": True},
    connection_options={"paths": [csv_path]},
    transformation_ctx="csv_data"
)


json_path = "s3://bucket-de-entrada/json/"
json_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": [json_path]},
    transformation_ctx="json_data"
)


consolidated_data = csv_data.union(json_data)


output_path = "s3://bucket-de-saida/dados-consolidados/"
glueContext.write_dynamic_frame.from_options(
    frame=consolidated_data,
    connection_type="s3",
    format="parquet",
    connection_options={"path": output_path},
    transformation_ctx="datasink"
)

job.commit()
