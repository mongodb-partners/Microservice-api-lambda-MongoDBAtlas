import os
import json
from pymongo import MongoClient
from bson import ObjectId

# Environment variables
ATLAS_CONNECTION_STRING = os.environ['ATLAS_CONNECTION_STRING']
COLLECTION_NAME = os.environ['COLLECTION_NAME']
DB_NAME = os.environ['DB_NAME']


def connect_to_mongodb():
    client = MongoClient(ATLAS_CONNECTION_STRING)
    return client

def success_response(body):
    return {
        'statusCode': '200',
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def error_response(err):
    error_message = str(err)
    return {
        'statusCode': '400',
        'body': error_message,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    client = None
    try:
        # Connect to MongoDB
        client = connect_to_mongodb()
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # CRUD operations
        operation = event['httpMethod']
        if operation == 'GET':
            payload = event.get('queryStringParameters') or {}
            if '_id' in payload:
                payload['_id'] = ObjectId(payload['_id'])
            response = list(collection.find(payload))
            for doc in response:
                doc['_id'] = str(doc['_id'])  
        else:
            payload = json.loads(event['body'])
            if operation == 'POST':
                insert_result = collection.insert_one(payload)
                response = {'_id': str(insert_result.inserted_id)}
            elif '_id' not in payload:
                return error_response(ValueError('_id is a required field in the body'))
            elif operation == 'PUT':
                document_id = ObjectId(payload['_id'])
                del payload['_id']
                response = collection.update_one({'_id': document_id}, {'$set': payload})
                response = {'modified_count': response.modified_count}
            elif operation == 'DELETE':
                response = collection.delete_one({'_id': ObjectId(payload['_id'])})
                response = {'deleted_count': response.deleted_count} 
            else:
                return error_response(ValueError('Unsupported method "{}"'.format(operation)))

        return success_response(response)

    except Exception as e:
        return error_response(e)

    finally:
        if client:
            client.close()
