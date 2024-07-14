# modules/aws/ec2.py

import boto3

def list_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    return instances
