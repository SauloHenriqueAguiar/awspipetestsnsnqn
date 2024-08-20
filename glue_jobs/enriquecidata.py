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

# Leitura dos dados do S3
input_path = "s3://bucket-de-entrada/dados-brutos/"
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    format_options={"withHeader": True},
    connection_options={"paths": [input_path]},
    transformation_ctx="datasource0"
)

# Limpeza dos dados
cleaned_data = datasource0.drop_nulls().drop_duplicates()

# Enriquecimento dos dados (Ex: adicionando uma nova coluna com informações calculadas)
enriched_data = cleaned_data.map(lambda row: row.update({"nova_coluna": row["coluna_existente"] * 2}))

# Escrita dos dados processados em um novo bucket
output_path = "s3://bucket-de-saida/dados-enriquecidos/"
glueContext.write_dynamic_frame.from_options(
    frame=enriched_data,
    connection_type="s3",
    format="parquet",
    connection_options={"path": output_path},
    transformation_ctx="datasink"
)

job.commit()
