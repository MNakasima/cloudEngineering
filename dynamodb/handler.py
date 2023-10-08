import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import uuid
import json


def handler(event, context):
    
    dao = BaseDAO('eventos-pizzaria')
    
    data = json.dumps(event)
    python_data = json.loads(data)
    
    dao.put_item( {
        'pedido': str(python_data['detail']['pedido']), 
        'status': python_data['detail']['status'], 
        'cliente': python_data['detail']['cliente'], 
        'time': str(datetime.now()) 
    })
    
    