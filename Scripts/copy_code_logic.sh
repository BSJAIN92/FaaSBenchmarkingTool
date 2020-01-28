#!/bin/bash

. ./config.sh

ls -l ../Code_Logic/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/code_logic

if [ "$FaaSBenchmarkRuntime" == aws-java-maven ]; then
    cp -r ../Code_Logic/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/code_logic ../Deployment/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/$FaaSBenchmarkServiceName/src/main/java/com/serverless
else
    cp -r ../Code_Logic/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/code_logic ../Deployment/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/$FaaSBenchmarkServiceName/
fi