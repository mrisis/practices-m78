from flask import Flask, jsonify, render_template
import pymongo
from pprint import pprint
import json

client = pymongo.MongoClient()
db = client.transaction
transaction = db.transaction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/show/<string:period>/<string:unit>')
def show_transaction(period, unit):
    global result
    vahed = 1
    if unit == 'toman':
        vahed = 0.1
    if period == 'yearly':
        filters = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year"}, "total": {"$sum": {'$multiply': ['$amount', vahed]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            filters
        )

    elif period == 'monthly':
        filters = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month"},
                        "total": {"$sum": {'$multiply': ['$amount', vahed]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            filters
        )


    elif period == 'daily':
        filters = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "day": {"$dayOfMonth": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month", "day": "$day"},
                        "total": {"$sum": {'$multiply': ['$amount', vahed]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            filters
        )

    elif period == 'weekly':
        filters = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "week": {"$week": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month", "week": "$week"},
                        "total": {"$sum": {'$multiply': ['$amount', vahed]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            filters
        )

    print(list(result))
    return str(list(result))


if __name__ == '__main__':
    app.run()
