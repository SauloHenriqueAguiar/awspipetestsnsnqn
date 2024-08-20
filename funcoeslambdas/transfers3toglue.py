import boto3

def lambda_handler(event, context):
    glue_client = boto3.client('glue')

    # Pega o nome do bucket e o nome do arquivo do evento S3
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Inicia o job do Glue
    response = glue_client.start_job_run(
        JobName='nome-do-seu-job-glue',
        Arguments={
            '--bucket_name': bucket_name,
            '--file_key': file_key
        }
    )

    return {
        'statusCode': 200,
        'body': f'Job do Glue iniciado com sucesso: {response["JobRunId"]}'
    }
