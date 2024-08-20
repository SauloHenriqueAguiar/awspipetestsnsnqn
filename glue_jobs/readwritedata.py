import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura dos dados do S3
input_path = "s3://bucket-de-entrada/caminho-do-arquivo/"
datasource0 = glueContext.create_dynamic_frame.from_options(
    format_options={"withHeader": True},
    connection_type="s3",
    format="csv",
    connection_options={"paths": [input_path]},
    transformation_ctx="datasource0"
)

# Transformação: por exemplo, filtro de colunas
transformed_data = datasource0.drop_fields(['coluna_desnecessaria'])

# Escrita dos dados transformados em um novo bucket
output_path = "s3://bucket-de-saida/caminho-de-destino/"
glueContext.write_dynamic_frame.from_options(
    frame=transformed_data,
    connection_type="s3",
    format="parquet",
    connection_options={"path": output_path},
    transformation_ctx="datasink"
)

job.commit()
