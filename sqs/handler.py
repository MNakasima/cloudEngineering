from sqsHandler import SqsHandler
import json

def handler(event, context):
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/603867557236/espera-entrega")
    
    data = json.dumps(event)
    python_data = json.loads(data)
    
    message = python_data['detail']['cliente'] + ' pedido: ' + str(python_data['detail']['pedido']) + python_data['detail']['status']
    
    sqs.send(message)
    
    return event