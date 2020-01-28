import json
from flask import jsonify, make_response
import sys
import time, datetime

def http(request):

    
    ExecutionStartTime = int(round(time.time() * 1000))
    
    sys.path.insert(0, '/code_logic')
    
    from code_logic import code_logic
    
    result = code_logic.code()
    
    ExecutionEndTime = int(round(time.time() * 1000))



    body = {
        "statusCode": 200,
        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "input": request,
        "res": result,
        "executionStart": ExecutionStartTime,
        "executionEnd": ExecutionEndTime
    }

    response = json.dumps(body)


    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    return (f'{response}', 200)

