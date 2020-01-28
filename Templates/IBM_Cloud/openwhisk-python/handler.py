import json
import sys
import time, datetime


def hello(params):

    
    ExecutionStartTime = int(round(time.time() * 1000))
    
    sys.path.insert(0, '/code_logic')
    
    from code_logic import code_logic
    
    result = code_logic.code()
    
    ExecutionEndTime = int(round(time.time() * 1000))



#    body = {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "input": event,
#        "res": result,
#        "ExecutionStart": ExecutionStartTime,
#        "ExecutionEnd": ExecutionEndTime
#    }

    response = {
        "statusCode": 200,
#        "body": json.dumps(body)
        "message": "Go Serverless v1.0! Your function executed successfully!",
#	"input": params,
	"res": result,
	"executionStart": ExecutionStartTime,
	"executionEnd": ExecutionEndTime
    }

    return response

#    name = params.get("name", "stranger")
#    greeting = "Hello " + name + "!"
#    print(greeting)
#    return {"greeting": greeting}
