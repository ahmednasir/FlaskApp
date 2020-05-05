from flask import Flask, request
app = Flask(__name__)
from services import dbServices
import datetime as dt
import uuid
import json
engine, model, session = dbServices.connect()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/', methods=["POST"])
def insertData():
    try:
        content = request.json
        path = content["path"]
        ip = content["ip"]
        modelObj = model()
        modelObj.Id = uuid.uuid1().hex
        modelObj.Address = ip
        modelObj.Path = path
        modelObj.CreatedOn = dt.datetime.now()
        session.add(modelObj)
        session.commit()

        return app.response_class(
            response=json.dumps({
                "Status":200,
                "Message":"Inserted"
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return app.response_class(
            response=json.dumps({
                "Status": 500,
                "Message": "NotInserted"
            }),
            status=200,
            mimetype='application/json'
        )

if __name__ == '__main__':
    if engine:
        app.run(port=3000)