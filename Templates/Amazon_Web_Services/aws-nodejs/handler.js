'use strict';

const code_logic = require("./code_logic");

module.exports.hello = async event => {
  const ExecutionStartTime = Date.now();
  const result = code_logic();
  const ExecutionEndTime = Date.now();
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: 'Go Serverless v1.0! Your function executed successfully!',
        input: event,
        res: result,
        executionStart: ExecutionStartTime,
        executionEnd: ExecutionEndTime,
      },
      null,
      2
    ),
  };

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};
