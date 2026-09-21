from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

table = boto3.resource(
    "dynamodb",
    region_name=os.environ["AWS_REGION"]
).Table("Customers")

@app.route("/")
def health():
    return "Customer API Running"

@app.route("/customer", methods=["POST"])
def create():
    data = request.json
    table.put_item(Item=data)
    return jsonify({"message":"Customer Created"})

@app.route("/customer/<customer_id>", methods=["GET"])
def read(customer_id):
    response = table.get_item(Key={"CustomerId":customer_id})
    return jsonify(response.get("Item",{}))

@app.route("/customer/<customer_id>", methods=["PUT"])
def update(customer_id):
    body=request.json
    table.update_item(
        Key={"CustomerId":customer_id},
        UpdateExpression="SET CustomerName=:n",
        ExpressionAttributeValues={
            ":n":body["CustomerName"]
        }
    )
    return jsonify({"message":"Updated"})
