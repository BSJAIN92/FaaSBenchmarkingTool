#!/bin/bash

# Select the provider you want to benchmark: "Amazon_Web_Services", "Google_Cloud_Platform", "IBM_Cloud"

FaaSBenchmarkProvider=""                 
    
#-----------------------------------------------
# Select a Runtime for your provider from the list given:
# Amazon_Web_Services: "aws-java-maven", "aws-nodejs", "aws-python3"
# Google_Cloud_Platform: "google-nodejs", "google-python"
# IBM_Cloud: "openwhisk-nodejs", "openwhisk-python"
# Copy and Paste the selected runtime below:
#-----------------------------------------------

FaaSBenchmarkRuntime=""

FaaSBenchmarkFunction="" # ConcurrencyRandomNumber - CalculateFibonacci - BackOffRandomNumber - EmptyFunction - Sleep

Name=""

FaaSBenchmarkServiceName="${Name}_${FaaSBenchmarkRuntime}_benchmark"

result_file_name="${FaaSBenchmarkProvider}_${FaaSBenchmarkRuntime}_${FaaSBenchmarkFunction}_${Name}_"
