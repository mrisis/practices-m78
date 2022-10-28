 

db.trips.find({
    'birth year':{$ne:''}

}).sort({'birth year':-1}).limit(1)
