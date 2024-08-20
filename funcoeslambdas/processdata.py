import json

def lambda_handler(event, context):
    
    for record in event['Records']:
        
        payload = json.loads(record['kinesis']['data'])
        
       
        print(f"Processed data: {payload}")

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }
