 
db.trips.find({"birth year":{"$gt":1998}}).count() - db.trips.find({"birth year":1998}).count()
