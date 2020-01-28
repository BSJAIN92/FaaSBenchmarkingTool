'use strict';

const code_logic = require("./code_logic");

exports.http = (request, response) => {
  const ExecutionStartTime = Date.now();
  const result = code_logic();
  const ExecutionEndTime = Date.now();
  
  

  response.status(200).send({
        message: "Go Serverless v1.0! Your function executed successfully!",
        //input: request,
        res: result,
        executionStart: ExecutionStartTime,
        executionEnd: ExecutionEndTime,
    });
};


exports.event = (event, callback) => {
  callback();
};
