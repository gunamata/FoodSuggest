import json
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor


def create(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
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
    conn.close()
    body = {
        "message": "FoodCategory Item has been inserted successfully!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response
    
def findAll(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM foodcategory'
    cursor.execute(psql)
    foodcategories = cursor.fetchall()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },             
        "body": json.dumps(foodcategories)
    }    
    return response   
    
def findOne(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    id = event['pathParameters']['Id']
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM foodcategory WHERE id = %s'
    cursor.execute(psql, (id,))
    foodcategory = cursor.fetchone()
    cursor.close()
    conn.close()
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },                
        "body": json.dumps(foodcategory)
    }    
    return response
    
def update(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    food_category = json.loads(event['body'])
    id = food_category['id']
    name = food_category['name']
    parentcategoryid = food_category['parentcategoryid']   
    cursor = conn.cursor()
    psql = 'UPDATE foodcategory set name = %s, parentcategoryid = %s WHERE id = %s'
    data = (name, parentcategoryid, id)
    cursor.execute(psql, data)
    conn.commit()
    cursor.close()
    conn.close()
    body = {
        "message": "foodcategory " + str(id) + " has been successfully updated!"
    }    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response
    
def delete(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    food_category = json.loads(event['body'])
    id = food_category['id']  
    cursor = conn.cursor()
    psql = 'DELETE FROM foodcategory WHERE id = %s'
    cursor.execute(psql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    body = {
        "message": "foodcategory " + str(id) + " has been successfully deleted!"
    }    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response    
    
    
   
    
    
    