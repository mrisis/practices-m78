 
db.listingsAndReviews.find({
    property_type:'House',
    amenities:{$in:['Changing table']}
}).count()
