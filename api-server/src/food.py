import json
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor

#DB Connection
conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")

def create(event, context):
    food_category = json.loads(event['body'])
    name = food_category['name']
    parentCategoryId = food_category['parentCategoryId']
    if parentCategoryId == "NULL":
    	parentCategoryId = None    
    cursor = conn.cursor()
    psql = '''INSERT INTO foodcategory (name, parentcategoryid) VALUES (%s,%s)'''
    data = (name, parentCategoryId)
    cursor.execute(psql, data)
    conn.commit()
    cursor.close()
    body = {
        "message": "FoodCategory Item has been inserted successfully!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response