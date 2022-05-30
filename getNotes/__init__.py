import logging
import azure.functions as func
import pymongo
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ["MyDbConnection"] # Change the Variable name, as applicable to you
        client = pymongo.MongoClient(url)
        database = client['lab2db'] # Change the MongoDB name
        collection = database['notes']    # Change the collection name

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except ConnectionError:
        logging.info("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
