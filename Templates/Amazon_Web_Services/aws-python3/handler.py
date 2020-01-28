import json
import sys
import time, datetime


def hello(event, context):
    
    
    ExecutionStartTime = int(round(time.time() * 1000))
    
    sys.path.insert(0, '/code_logic')
    
    from code_logic import code_logic
    
    result = code_logic.code()
    
    ExecutionEndTime = int(round(time.time() * 1000))



    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "res": result,
        "executionStart": ExecutionStartTime,
        "executionEnd": ExecutionEndTime
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

