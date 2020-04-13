import json
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor


def findAll(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM disease'
    cursor.execute(psql)
    diseases = cursor.fetchall()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },           
        "body": json.dumps(diseases)
    }    
    return response   
    
def findOne(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    id = event['pathParameters']['Id'];
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM disease WHERE id = %s'
    cursor.execute(psql, (id,))
    disease = cursor.fetchone()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },           
        "body": json.dumps(disease)
    }    
    return response