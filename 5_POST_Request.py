   # POST Request -> Create new data
import requests


        # lnik API URL
link = "https://jsonplaceholder.typicode.com/posts";


    # Create new data
data = {
    "title" : "Python For Fast API",
    "body" : "Learning REST API",
    "userId" : 1,
};


respone = requests.get(link, json=data)

   # Display
print(respone.status_code);
print(respone.json());