# myapp/views.py
# myapp/views.py
# myapp/views.py
# myapp/views.py
from django.shortcuts import render
from pymongo import MongoClient

def homepage(request):
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)  # Assuming MongoDB is running on the default port
    db = client['Jobs']
    collection = db['Indeed']

    # Retrieve data from MongoDB
    job_listings = collection.find()

    return render(request, 'myapp/homepage.html', {'job_listings': job_listings})
