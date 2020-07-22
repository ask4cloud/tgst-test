#!/home/centos/projects/tgw-aws-stno/source/env/bin/python

from state_machine_handler_test import VPC, DynamoDb, ResourceAccessManager, ApprovalNotification
from lib.logger import Logger
import os
import inspect
import os.path
import sys
import json

# initialise logger
LOG_LEVEL = "WARN" 
logger = Logger(loglevel=LOG_LEVEL)

import botocore
import boto3

with open('./sample_event.json') as f:
  event = json.load(f)

print('Event Before: ', event)

vpc = VPC(event, logger)
response = vpc.describe_resources()
print()
print('Event After: ', event)
#print(response)


