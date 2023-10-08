from sqsHandler import SqsHandler
from env import Variables
import json

def handler(event,context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    
    for i in range(100):
        msgs = sqs.getMessage(10)
        print(json.dumps(msgs))
        
        if('Messages' not in msgs):
            break
        if(len(msgs['Messages'])==0):
            break
        
        for message in msgs['Messages']:
            sqs.deleteMessage(message['ReceiptHandle'])