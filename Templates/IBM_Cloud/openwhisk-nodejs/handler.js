'use strict';

const code_logic = require("./code_logic");

function hello(params) {
  const ExecutionStartTime = Date.now();

//  const name = params.name || 'World';

  const result = code_logic();

  const ExecutionEndTime = Date.now();

//  console.log('log', { payload: `Hello, ${name}` });

//  return { payload: `Hello, ${name}!` };

  return {
    statusCode: 200,
//    body: JSON.stringify(
//      {
        message: 'Go Serverless v1.0! Your function executed successfully!',
        input: params,
        res: result,
        executionStart: ExecutionStartTime,
        executionEnd: ExecutionEndTime,
//      },
//      null,
//      2
//    ),
  };



}

exports.hello = hello;
