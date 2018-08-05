# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='test1-bucket-hemaraj-4-python-boto3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec_client = session.client('ec2')
ec_client
get_ipython().run_line_magic('histiry', '')
get_ipython().run_line_magic('history', '')
