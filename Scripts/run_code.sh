#!/bin/bash

. ./config.sh

cd ../Deployment/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/$FaaSBenchmarkServiceName

pwd

if [ "$FaaSBenchmarkProvider" == Amazon_Web_Services ]; then
    target_url=$(sls info -r eu-west-2 | egrep -o 'https?://[^ ]+' | head -1)
elif [ "$FaaSBenchmarkProvider" == Google_Cloud_Platform ]; then
    target_url=$(sls info -r europe-west2 | egrep -o 'https?://[^ ]+' | head -1)
elif [ "$FaaSBenchmarkProvider" == IBM_Cloud ]; then
    target_url=$(sls info -r eu-gb | egrep -o 'https?://[^ ]+' | head -1)
fi

echo $target_url

cd ~/FaaSBenchmarkingTool/Scripts/


env url=$target_url env file_name=$result_file_name locust -f locustfile.py --host https://localhost:5000 --no-web -c 1 -r 1 --run-time 28000s --csv=../Results/LocustGenerated/$result_file_name

#echo $result_file_name
