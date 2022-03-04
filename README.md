Exercise 04.03.22
Exercise to learn the Basics about python and apis

We will build da dashboard for corona data

1. Setup project
create a new git repository
2. create a python script that use the corona api to provide dashboard data
use python to call the rest api to get the latest corona data for germany
save a json file that looks like the following.
{
    "cases":12345,
    "active": 234,
    "trend": "UP",
    "lockdown": true
}

cases: are all cases
active: currently infectet
trend: active cases increases or decreasing over the last 7 days
lockdown: active over last 7 days over 10.000
Use the python sdk to upload the result corona-data.json to an s3 bucket
3. terraform (optional)
create a terraform project that setup an ec2 instance with python and runs your script every 10 minutes automatically
4. CD (optional)
Setup a github actions pipeline that deploys your code and infrastructure