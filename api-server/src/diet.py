# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:23:59 2020

@author: Guna
"""

import boto3
import os.path
import os
import json
import pandas as pd

strLocalTempDir = '/tmp/input/'

#Download Excel from S3 to /tmp/input
def get_master_data(strBucket, strBucketKey,strDietFilename):
    global  strLocalTempDir

    if not os.path.exists(strLocalTempDir):
        os.makedirs(strLocalTempDir)
    src = strBucketKey + '/' + strDietFilename
    dest = strLocalTempDir + strDietFilename
    bucket = boto3.resource('s3').Bucket(strBucket)
    print(src)
    print(dest)
    print("Before download statement")
    bucket.download_file(src, dest)
    print("After download statement")
    return dest
    
def load_from_excel(event, context):
    print(event)
    input = event['body']
    input_dict = json.loads(input)
    strBucket = input_dict['bucket_name']
    strBucketKey = input_dict['bucket_key']
    strDietFilename = input_dict['data_file_name']
    
    #strBucket = "foodsuggest"
    #strBucketKey = "master/"
    #strDietFilename = "diets_list.xlsx"    
    
    print(strBucket)
    print(strBucketKey)
    print(strDietFilename)

    dest = get_master_data(strBucket, strBucketKey,strDietFilename)
    print(dest)
    
    #Read Excel
    df = pd.read_excel(dest)
    
    body = {
        "message": "Loaded Excel into Dataframe",
        "input": df
    }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    print(response)

    return response



       
    