 
db.trips.find({
    $and:[

    {'start station location.coordinates':{$lt:-74.0}},
    {'start station location.coordinates':{$gt:-75.0}}
    ]

}).count()
