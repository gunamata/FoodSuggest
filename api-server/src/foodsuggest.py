import json
import psycopg2
from psycopg2.extras import RealDictCursor


def foodsuggest(event,context):
    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    diet = event['pathParameters']['Diet']
    disease = event['pathParameters']['Disease']
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM food WHERE \
	    id IN (SELECT food_id FROM dietrecommendation WHERE recommended = 1 AND diet_id = (SELECT id FROM diet WHERE name = %s)) AND \
	    id NOT IN (SELECT food_id FROM dietrecommendation WHERE recommended = 0 AND diet_id = (SELECT id FROM diet WHERE name = %s)) AND \
	    id IN (SELECT food_id FROM diseaserecommendation WHERE recommended = 1 AND disease_id = (SELECT id FROM disease WHERE name = %s)) AND \
	    id NOT IN (SELECT food_id FROM diseaserecommendation WHERE recommended = 0 AND disease_id = (SELECT id FROM disease WHERE name = %s))'
    cursor.execute(psql, (diet,diet,disease,disease))
    foodsuggestions = cursor.fetchall()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },           
        "body": json.dumps(foodsuggestions)
    }    
    return response
    
def foodsuggestforinputjson(event,context):
    searchOptions = json.loads(event['body'])
    diets = searchOptions['diets']
    diseases = searchOptions['diseases']

    diets_list_len = len(diets)
    diet_placeholder = ''
    
    for i in range(diets_list_len):
        diet_placeholder = diet_placeholder + '\'' + diets[i] + '\''
        if(i < len(diets)-1):
            diet_placeholder = diet_placeholder + ', '
            
    diseases_list_len = len(diets)
    disease_placeholder = ''
    
    for i in range(diseases_list_len):
        disease_placeholder = disease_placeholder + '\'' + diseases[i] + '\''
        if(i < len(diseases)-1):
            disease_placeholder = disease_placeholder + ', '

    #DB Connection
    conn = psycopg2.connect("dbname='foodsuggest' host='foodsuggest.co04tmhhaeuf.us-east-1.rds.amazonaws.com' user='postgres' password='postgres' port='5432'")
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    psql = 'SELECT * FROM food WHERE ' + \
    	   'id IN (SELECT food_id FROM dietrecommendation WHERE recommended = 1 AND diet_id IN (SELECT id FROM diet WHERE name IN (' + diet_placeholder + '))) AND ' + \
           'id NOT IN (SELECT food_id FROM dietrecommendation WHERE recommended = 0 AND diet_id IN (SELECT id FROM diet WHERE name IN (' + diet_placeholder + '))) AND ' + \
           'id IN (SELECT food_id FROM diseaserecommendation WHERE recommended = 1 AND disease_id IN (SELECT id FROM disease WHERE name IN (' + disease_placeholder + '))) AND ' + \
           'id NOT IN (SELECT food_id FROM diseaserecommendation WHERE recommended = 0 AND disease_id IN (SELECT id FROM disease WHERE name IN (' + disease_placeholder + ')))'
    cursor.execute(psql)
    foodsuggestions = cursor.fetchall()
    cursor.close()
    conn.close()   
    response = {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" , "Access-Control-Allow-Origin": '*' },           
        "body": json.dumps(foodsuggestions)
    }    
    return response    