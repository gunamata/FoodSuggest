import json
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor


def create(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    food = json.loads(event['body'])
    name = food['name']
    categoryid = food['categoryid']
    if categoryid == "NULL":
    	categoryid = None    
    cursor = conn.cursor()
    psql = '''INSERT INTO food (name, categoryid) VALUES (%s,%s)'''
    data = (name, categoryid)
    cursor.execute(psql, data)
    conn.commit()
    cursor.close()
    conn.close()
    body = {
        "message": "Food Item has been inserted successfully!"
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
    psql = 'SELECT * FROM food'
    cursor.execute(psql)
    foods = cursor.fetchall()
    cursor.close()
    conn.close()
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },           
        "body": json.dumps(foods)
    }    
    return response   
    
def findOne(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    id = event['pathParameters']['Id'];
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM food WHERE id = %s'
    cursor.execute(psql, (id,))
    food = cursor.fetchone()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },               
        "body": json.dumps(food)
    }    
    return response
    
def update(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    food = json.loads(event['body'])
    id = food['id']
    name = food['name']
    categoryid = food['categoryid']   
    cursor = conn.cursor()
    psql = 'UPDATE food set name = %s, categoryid = %s WHERE id = %s'
    data = (name, categoryid, id)
    cursor.execute(psql, data)
    conn.commit()
    cursor.close()
    conn.close()
    body = {
        "message": "food " + str(id) + " has been successfully updated!"
    }    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response
    
def delete(event, context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    food = json.loads(event['body'])
    id = food['id']  
    cursor = conn.cursor()
    psql = 'DELETE FROM food WHERE id = %s'
    cursor.execute(psql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    body = {
        "message": "food " + str(id) + " has been successfully deleted!"
    }    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }    
    return response