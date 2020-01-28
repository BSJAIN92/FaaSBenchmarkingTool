#!/bin/bash

. ./config.sh

cd ../Deployment/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/$FaaSBenchmarkServiceName

pwd

if [ "$FaaSBenchmarkRuntime" == aws-java-maven ]; then
    mvn package
fi


if [ "$FaaSBenchmarkProvider" == Amazon_Web_Services ]; then
    sls deploy -r eu-west-2
elif [ "$FaaSBenchmarkProvider" == Google_Cloud_Platform ]; then
    npm install
    sls remove -r europe-west-2
    sls deploy -r europe-west2
elif [ "$FaaSBenchmarkProvider" == IBM_Cloud ]; then
    npm install
    ibmcloud wsk property get --auth
    sls deploy -r eu-gb
fi


cd ~/FaaSBenchmarkingTool/Scripts/
