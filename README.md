# locust-load-testing
Locust load testing using docker

## Setup and Running the test

Run the docker compose file. Add `-d` at the end if you want to run it in detached mode.

`docker-compose up -d`

Web UI will be hosted in localhost port 8089:

[Web UI](#localhost:8089)

Run the test using web UI. The results can be observed in the Web UI. 

Additionally, we are outputting the result data to csv file inside locust/results folder.


## Summary
>The -f/--locustfile option accepts a single directory of locustfiles as an option. Locust will recursively search the directory for *.py files, ignoring files named locust.py or those that start with “_”.

We are using `-f /locust/locustfiles` (`-f /mnt/locust/locustfiles` inside container) as our locust files location.