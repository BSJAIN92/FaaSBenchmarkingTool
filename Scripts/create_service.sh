#!/bin/bash

. ./config.sh

sls create --template-path ../Templates/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime --path ../Deployment/$FaaSBenchmarkProvider/$FaaSBenchmarkRuntime/$FaaSBenchmarkFunction/$FaaSBenchmarkServiceName -n $Name
